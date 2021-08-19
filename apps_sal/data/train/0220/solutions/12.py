class Solution:

    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        curr_sum = sum([i * abs(j - 1) for (i, j) in zip(customers, grumpy)])
        max_sum = curr_sum
        for i in range(X):
            curr_sum += customers[i] * grumpy[i]
            max_sum = max(max_sum, curr_sum)
        for i in range(1, len(customers) - X + 1):
            max_sum = max(max_sum, curr_sum)
            curr_sum -= customers[i - 1] * grumpy[i - 1]
            curr_sum += customers[i + X - 1] * grumpy[i + X - 1]
        return max(max_sum, curr_sum)
