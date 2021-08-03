class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l, h = 1, max(piles)

        def canFinish(k):
            hoursTaken = sum([ceil(p / k) for p in piles])
            return hoursTaken <= H

        while l < h:
            mid = l + (h - l) // 2
            if canFinish(mid):
                h = mid
            else:
                l = mid + 1
        return l
