class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        (left, right) = (max(weights), sum(weights))
        while left < right:
            mid = (left + right) // 2
            if self.can_achieve(weights, mid, D):
                right = mid
            else:
                left = mid + 1
        return left

    def can_achieve(self, weights, max_weight, D):
        i = 0
        total = 0
        days = 0
        while i < len(weights):
            if total + weights[i] > max_weight:
                total = 0
                days += 1
            total += weights[i]
            i += 1
        days += 1
        return days <= D
