from collections import deque


class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:

        def canShip(capacity):
            nonlocal D
            (count, loaded) = (1, 0)
            for w in weights:
                if loaded + w <= capacity:
                    loaded += w
                else:
                    count += 1
                    loaded = w
            return count <= D
        max_weight = max(weights)
        (low, high) = (sum(weights) // D, max_weight * len(weights) // D + 1)
        while low < high:
            mid = low + (high - low) // 2
            if mid < max_weight or not canShip(mid):
                low = mid + 1
            else:
                high = mid
        return low
