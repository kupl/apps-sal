class Solution:
    def canShipAllPackages(self, weight_capacity, D, weights):
        # print(f\"weight_capacity: {weight_capacity}\")

        days_needed = 1
        current_day_weight = 0
        i = 0
        while i < len(weights):
            weight = weights[i]
            # print(f\"weight: {weight}\")
            if (current_day_weight + weight) <= weight_capacity:
                current_day_weight += weight
                # print(f\"Day {days_needed}, current_day_weight: {current_day_weight}\")
                i += 1
            else:
                # print(f\"Too much! Next day work\")
                current_day_weight = 0
                days_needed += 1
                
        # print(\"f{days_needed}\")
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
