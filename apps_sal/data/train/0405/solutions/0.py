class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp = [0] * (N + W)
        for i in range(K, N + 1):
            dp[i] = 1

        S = min(W, N - K + 1)
        for i in range(K - 1, -1, -1):
            dp[i] = S / W
            S += dp[i] - dp[i + W]
        return dp[0]
