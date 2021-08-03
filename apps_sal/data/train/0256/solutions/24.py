import math


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l = 1
        r = max(piles)
        while l <= r:
            m = l + (r - l) // 2
            if calc_h(piles, m) > H:
                l = m + 1
            else:  # calc_h(piles, m) <= H
                if m == 1 or calc_h(piles, m - 1) > H:
                    return m
                r = m - 1


def calc_h(piles, K):
    h = [p // K + (p % K > 0) for p in piles]
    return int(sum(h))
