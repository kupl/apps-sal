class Solution:

    def possibleWithinDays(self, weights, D, capacity):
        x = 0
        i = 1
        total = 0
        while i <= D:
            current_sum = 0
            while x < len(weights) and current_sum + weights[x] <= capacity:
                current_sum += weights[x]
                total += weights[x]
                x += 1
            i += 1
        if total >= sum(weights):
            return True
        return False

    def shipWithinDays(self, weights: List[int], D: int) -> int:
        total_sum = sum(weights)
        left = 0
        right = total_sum
        while left < right:
            middle = (left + right) // 2
            aux = self.possibleWithinDays(weights, D, middle)
            if aux:
                right = middle
            else:
                left = middle + 1
        return left
