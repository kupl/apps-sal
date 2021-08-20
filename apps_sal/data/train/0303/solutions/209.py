class Solution:

    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        memo = {}

        def getMax(arr, k, idx):
            if idx == len(arr):
                return 0
            if idx in memo:
                return memo[idx]
            (maxSum, maxInSub) = (0, 0)
            for i in range(idx, min(idx + K, len(arr))):
                maxInSub = max(maxInSub, arr[i])
                maxSum = max(maxSum, maxInSub * (i - idx + 1) + getMax(arr, k, i + 1))
            memo[idx] = maxSum
            return maxSum
        return getMax(A, K, 0)
