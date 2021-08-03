class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        # O(N + W), https://www.youtube.com/watch?v=bd0t6cj7_4E
        # Let dp(x) be the answer when we already have x points.
        dp = [0] * (N + W + 1)

        for i in range(K, N + 1):
            dp[i] = 1.0

        s = N - K + 1  # How many 1.0s
        # dp[k] = 1 / W * (dp[k+1] + dp[k+2] + ... + dp[k+W])
        for i in range(K - 1, -1, -1):
            dp[i] = s / W
            # s = 0
            # for j in range(W):
            # s += dp[i + j + 1]
            # dp[i] = s / W
            s += dp[i] - dp[i + W]

        return dp[0]
