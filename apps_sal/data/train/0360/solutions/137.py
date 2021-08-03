import sys


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = left * len(weights) // D
        while left < right:
            mid = left + (right - left) // 2
            c = 0  # capacity
            d = 1  # days
            for w in weights:
                if c + w <= mid:
                    c += w
                else:
                    d += 1
                    c = w
            if d > D:
                left = mid + 1
            else:
                right = mid
        return left
