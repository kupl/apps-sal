class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        maxSum = A[0]
        minSum = A[0]
        currMax = 0
        currMin = 0
        total = 0
        for a in A:
            currMax = max(currMax + a, a)
            maxSum = max(currMax, maxSum)
            currMin = min(currMin + a, a)
            minSum = min(currMin, minSum)
            total += a
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum
