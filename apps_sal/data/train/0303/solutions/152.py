class Solution:

    def maxSumAfterPartitioning(self, arr, k):
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(n):
            cmax = 0
            for j in range(1, min(k, i + 1) + 1):
                cmax = max(cmax, arr[i - j + 1])
                dp[i] = max(dp[i], dp[i - j] + cmax * j)
        return dp[-2]
