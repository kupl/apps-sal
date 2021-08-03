import math


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def check(avg):
            return sum(math.ceil(i / avg) for i in piles) <= H
        hi, lo = max(piles), 1
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return hi


1
