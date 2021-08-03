class Solution:
    def minEatingSpeed(self, piles, H):
        import math
        left = 1
        right = math.ceil(max(piles) * len(piles) / H)
        while left < right:
            mid = left + (right - left) // 2
            if self.f(piles, mid) > H:
                left = mid + 1
            else:
                right = mid

        return left

    def f(self, piles, K):
        import math
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / K)
        return hours
