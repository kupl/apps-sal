import math


class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        def compute_hours(piles, K):
            ret = 0
            for p in piles:
                ret += math.ceil(p / K)
            return ret
        lo = 1
        hi = sum(piles)
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            val = compute_hours(piles, mid)
            if val <= H:
                hi = mid - 1
            else:
                lo = mid
        if compute_hours(piles, hi) <= H:
            return hi
        else:
            return hi + 1
