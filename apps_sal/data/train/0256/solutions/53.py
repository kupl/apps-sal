import math


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        def is_smaller_equal_H(piles, K, H):
            ret = 0
            for p in piles:
                ret += math.ceil(p / K)
                if ret > H:
                    return False
            return True

        # descending, larger K, smaller hours; smaller K, larger hours
        # find smallest K, where h <= H
        # result K - 1 should be invalid, since K is the smallest valid value
        lo = 1
        hi = sum(piles)
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            flag = is_smaller_equal_H(piles, mid, H)
            if flag:  # K might be smaller
                hi = mid - 1
            else:  # too small
                lo = mid
        if is_smaller_equal_H(piles, hi, H):  # happens when hi == original lo
            return hi
        else:
            return hi + 1
