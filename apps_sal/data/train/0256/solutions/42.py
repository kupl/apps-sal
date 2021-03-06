class Solution:

    def minEatingSpeed(self, piles, H):
        (lo, hi) = (1, max(piles))
        while lo <= hi:
            K = lo + (hi - lo >> 1)
            if self.countTimeEatAllAtSpeed(K, piles) <= H:
                hi = K - 1
            else:
                lo = K + 1
        return lo

    def countTimeEatAllAtSpeed(self, K, piles):
        countHours = 0
        for pile in piles:
            countHours += pile // K
            if pile % K != 0:
                countHours += 1
        return countHours
