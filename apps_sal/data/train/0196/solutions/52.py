class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        maxSum = curSum = A[0]
        for i in range(1, len(A)):
            curSum = max(A[i], A[i] + curSum)
            maxSum = max(maxSum, curSum)

        if maxSum < 0:
            return maxSum

        minSum = curSum = A[0]
        for i in range(1, len(A)):
            curSum = min(A[i], A[i] + curSum)
            minSum = min(minSum, curSum)

        return max(sum(A) - minSum, maxSum)
