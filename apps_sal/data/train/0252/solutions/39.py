class Solution:

    def minTaps(self, n, A):
        dp = [0] + [n + 2] * n
        for (i, x) in enumerate(A):
            for j in range(max(i - x + 1, 0), min(i + x, n) + 1):
                dp[j] = min(dp[j], dp[max(0, i - x)] + 1)
        return dp[n] if dp[n] < n + 2 else -1
