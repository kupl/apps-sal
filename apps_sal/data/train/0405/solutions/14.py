class Solution:

    def new21Game(self, N: int, K: int, W: int) -> float:
        if N < K:
            return 0
        if N > K - 1 + W:
            return 1
        dp = [0] * (K + W)
        for k in range(K, N + 1):
            dp[k] = 1
        S = N - K + 1
        for k in range(K - 1, -1, -1):
            dp[k] = S / W
            S += dp[k] - dp[k + W]
        return dp[0]
