class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        maxSum = A[0]
        curMaxSum = A[0]
        for i in range(1, len(A)):
            curMaxSum = max(curMaxSum + A[i], A[i])
            maxSum = max(maxSum, curMaxSum)
        minSum = A[0]
        curMinSum = A[0]
        for i in range(1, len(A)):
            curMinSum = min(curMinSum + A[i], A[i])
            minSum = min(minSum, curMinSum)
        if maxSum < 0:
            return maxSum
        return max(maxSum, sum(A) - minSum)
