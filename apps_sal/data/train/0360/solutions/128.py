class Solution:

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        self.weights = weights
        self.days = days
        (left, right) = (max(weights), sum(weights))
        while left < right:
            mid = left + (right - left) // 2
            if self.isFit(mid):
                right = mid
            else:
                left = mid + 1
        return left

    def isFit(self, capacity):
        weight_index = 0
        for day in range(0, self.days):
            current_capacity = capacity
            while current_capacity >= 0:
                if weight_index == len(self.weights):
                    return True
                weight = self.weights[weight_index]
                if current_capacity - weight < 0:
                    break
                else:
                    current_capacity -= weight
                    weight_index += 1
        return False
