class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        total = sum(A)
        minSum = self.maxSum([-x for x in A]) + total
        maxSum = self.maxSum(A)
        return max(maxSum, minSum) if minSum > 0 else maxSum

    def maxSum(self, A: List[int]) -> int:
        current = 0
        max_sum = float('-inf')
        for num in A:
            current += num
            if current > max_sum:
                max_sum = current
            if current < 0:
                current = 0
        return max_sum
