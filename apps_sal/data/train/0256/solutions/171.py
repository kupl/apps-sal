import math


class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            K = (left + right) // 2
            hours = 0
            for pile in piles:
                if pile <= K:
                    hours += 1
                else:
                    hours += math.ceil(pile / K)
            if hours > H:
                left = K + 1
            else:
                right = K
        return left
