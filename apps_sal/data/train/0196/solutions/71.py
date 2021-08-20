import numpy as np


class Solution:

    def maxSubarraySumCircular(self, A: List[int]) -> int:
        (total, maxSum, curMax, minSum, curMin) = (0, A[0], -np.Infinity, A[0], np.Infinity)
        for a in A:
            curMax = max(curMax + a, a)
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + a, a)
            minSum = min(minSum, curMin)
            total += a
        return max(maxSum, total - minSum) if maxSum > 0 else maxSum
