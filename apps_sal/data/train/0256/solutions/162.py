# upper_bound: max(piles)
# lower_bound: ceil(sum(piles) / H)

import math


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left = math.ceil(sum(piles) / H)
        right = max(piles)

        while left <= right:
            middle = (left + right) // 2
            if is_valid(piles, H, middle):
                right = middle - 1
            else:
                left = middle + 1

        return left


def is_valid(piles, H, speed):
    hour = 0
    for pile in piles:
        hour += math.ceil(pile / speed)
    return hour <= H
