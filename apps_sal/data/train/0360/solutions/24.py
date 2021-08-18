class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:

        n = len(weights)

        def canShipWithCap(cap):
            d = 1
            w = 0
            for i in range(0, n):
                if weights[i] + w <= cap:
                    w += weights[i]
                else:
                    w = weights[i]
                    d += 1
                    if d > D:
                        return False
            return True

        high = sum(weights)
        low = max(weights)

        while low < high:

            mid = low + (high - low) // 2
            if canShipWithCap(mid):
                high = mid
            else:
                low = mid + 1

        return low
