class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        def time(val):
            t = len(piles)
            for pile in piles:
                t += (pile - 1) // val
            return t
        s = sum(piles)
        (l, r) = (math.ceil(s / H), math.ceil(s / (H - len(piles) + 1)))
        while l <= r:
            mid = l + (r - l) // 2
            t = time(mid)
            if t <= H:
                r = mid - 1
            else:
                l = mid + 1
        return l
