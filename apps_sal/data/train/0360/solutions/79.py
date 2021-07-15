class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def ship_capacity(weights, D, capacity):
            days = 0
            sum_weights = 0
            for i in range(len(weights) - 1):
                sum_weights += weights[i]
                if sum_weights + weights[i + 1] > capacity:
                    days += 1
                    sum_weights = 0
            return days <= D - 1
        start = max(weights)
        end = sum(weights)
        while start <= end:
            mid = (start + end) // 2
            if ship_capacity(weights, D, mid):
                end = mid - 1
            else:
                start = mid + 1
        return start
