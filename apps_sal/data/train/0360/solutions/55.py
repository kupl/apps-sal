class Solution:

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = sum(weights) + 1
        while left < right:
            mid = left + (right - left) // 2
            legal = self.evaluate(weights, D, mid)
            if legal:
                right = mid
            else:
                left = mid + 1
        return left

    def evaluate(self, weights, D, weight_capacity):
        cursum = 0
        days = 0
        for val in weights:
            if val > weight_capacity:
                return False
            if val + cursum > weight_capacity:
                days += 1
                cursum = val
            else:
                cursum += val
        if cursum != 0:
            days += 1
        if days > D:
            return False
        return True
