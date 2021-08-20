class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        (total, maxSum) = (0, A[0])
        (curMax, minSum, curMin) = (0, A[0], 0)
        for a in A:
            curMax = max(curMax + a, a)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + a, a)
            minSum = min(minSum, curMin)
            total += a
        return max(maxSum, total - minSum) if total != minSum else maxSum
