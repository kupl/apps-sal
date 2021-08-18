class Solution:
    def canShipAllPackages(self, weight_capacity, D, weights):

        days_needed = 1
        current_day_weight = 0
        i = 0
        while i < len(weights):
            weight = weights[i]
            if (current_day_weight + weight) <= weight_capacity:
                current_day_weight += weight
                i += 1
            else:
                current_day_weight = 0
                days_needed += 1

        return days_needed <= D

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        if len(weights) == 0:
            return 0

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2
            if self.canShipAllPackages(mid, D, weights):
                right = mid
            else:
                left = mid + 1

        return left
