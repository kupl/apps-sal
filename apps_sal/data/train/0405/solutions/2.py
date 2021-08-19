class Solution:

    def new21Game(self, N: int, K: int, W: int) -> float:
        dp = [0.0] * (N + W + 1)
        for k in range(K, N + 1):
            dp[k] = 1.0
        S = sum((dp[i] for i in range(K, K + W + 1)))
        for k in reversed(list(range(K))):
            dp[k] = S / float(W)
            S += dp[k] - dp[k + W]
        return dp[0]
