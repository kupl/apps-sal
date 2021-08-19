from typing import List
from math import ceil


class Solution:

    def minEatingSpeed(self, piles: List[int], H: int) -> int:

        def get_hours(piles, K):
            total = 0
            for num in piles:
                total += ceil(num / K)
            return total
        (left, right) = (1, max(piles))
        while left < right:
            mid = left + (right - left) // 2
            if get_hours(piles, mid) > H:
                left = mid + 1
            else:
                right = mid
        return left
