import math


class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        if H == len(piles):
            return max(piles)

        def possible(K):
            return sum((math.ceil(p / K) for p in piles)) <= H
        (lo, hi) = (1, max(piles))
        while lo < hi:
            print(lo, hi)
            mi = (lo + hi) // 2
            if not possible(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo
