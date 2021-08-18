class Solution:
    def printm(self, arr):
        [print(arr[i]) for i in range(len(arr))]

    def maxSumAfterPartitioning(self, A, K):
        size = len(A)
        dp = [0] * size
        for i in range(K):
            dp[i] = max(A[:i + 1]) * (i + 1)

        for i in range(K, size):
            for j in range(1, K + 1):
                dp[i] = max(dp[i], dp[i - j] + max(A[i - j + 1:i + 1]) * j)
        return dp[-1]
