class Solution:
    def maxSumAfterPartitioning(self, A: List[int], k: int) -> int:
        N = len(A)
        dp = [0] * (N + 1)

        for i in range(N):
            mx = 0
            for j in range(i, max(-1, i - k), -1):
                mx = max(mx, A[j])
                p = dp[i + 1]
                dp[i + 1] = max(dp[i + 1], dp[j] + mx * (i - j + 1))
        return dp[N]
