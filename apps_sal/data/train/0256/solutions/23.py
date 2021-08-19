import math


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        self.store = {}

        l = 1
        r = max(piles)
        while l <= r:
            m = l + (r - l) // 2
            if self.calc_h(piles, m) > H:
                l = m + 1
            else:  # calc_h(piles, m) <= H
                if m == 1 or self.calc_h(piles, m - 1) > H:
                    return m
                r = m - 1

    def calc_h(self, piles, K):
        if K not in self.store:
            h = [p // K + (p % K > 0) for p in piles]
            self.store[K] = int(sum(h))
        return self.store[K]
