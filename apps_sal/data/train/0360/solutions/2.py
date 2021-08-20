class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:

        def canShip(capacity: int) -> bool:
            nonlocal D
            count = 1
            curcap = 0
            for w in weights:
                if curcap + w <= capacity:
                    curcap += w
                else:
                    count += 1
                    curcap = w
            return count <= D
        max_weight = max(weights)
        lo = sum(weights) // D
        hi = max_weight * (len(weights) // D + 1)
        while lo < hi:
            mid = (lo + hi) // 2
            if mid < max_weight or not canShip(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo
