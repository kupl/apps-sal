class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = max(weights), max(weights) * len(weights) // D

        def checkShipping(capacity):
            days = 1
            total_weight = 0
            for weight in weights:
                if weight > capacity or days > D:
                    return False
                if weight + total_weight > capacity:
                    total_weight = weight
                    days += 1
                else:
                    total_weight += weight
            return days <= D

        while left <= right:
            mid = left + (right - left) // 2
            if checkShipping(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
