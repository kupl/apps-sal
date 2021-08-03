class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l = max(sum(piles) // H, 1)
        h = max(piles)
        while l < h:
            mid = (l + h) // 2
            timeL = self.timeTaken(piles, l)
            timeMid = self.timeTaken(piles, mid)
            if timeL <= H:
                return l
            elif timeMid <= H:
                h = mid
                timeH = timeMid
                l += 1
            else:
                l = mid + 1
        return l

    def timeTaken(self, piles, n):
        summ = 0
        for v in piles:
            summ += v // n
            if v % n:
                summ += 1
        return summ
