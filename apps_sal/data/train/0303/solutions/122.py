class Solution:

    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        n = len(A)
        dp = [0] * (n + 1)
        for i in range(n):
            for k in range(1, K + 1):
                if i - k > -2:
                    dp[i + 1] = max(dp[i + 1], max(A[max(0, i - k + 1):i + 1]) * k + dp[i + 1 - k])
        return dp[n]
