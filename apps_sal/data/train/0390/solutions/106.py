class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = any(not dp[i - j**2] for j in range(1, int(i ** 0.5) + 1))
        return dp[-1]
