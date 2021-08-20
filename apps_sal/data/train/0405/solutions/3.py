class Solution1:

    def new21Game(self, N: int, K: int, W: int) -> float:
        dp = [None] * (K + W)
        s = 0
        for i in range(K, K + W):
            dp[i] = 1 if i <= N else 0
            s += dp[i]
        for i in range(K - 1, -1, -1):
            dp[i] = s / W
            s = s - dp[i + W] + dp[i]
        return dp[0]


class Solution:

    def new21Game(self, N: int, K: int, W: int) -> float:
        dp = [1 if i <= N else 0 for i in range(K + W)]
        s = sum(dp[K:K + W])
        for i in range(K - 1, -1, -1):
            dp[i] = s / W
            s = s - dp[i + W] + dp[i]
        return dp[0]
