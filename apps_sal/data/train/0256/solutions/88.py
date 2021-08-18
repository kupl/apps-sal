import math


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        def feasible(maxBananas):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / maxBananas)

                if hours > H:
                    return False
            return True

        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2

            if feasible(mid):
                right = mid
            else:
                left = mid + 1

        return left
