class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        dp[1] = True
        for i in range(2, n + 1):
            dp[i] = not all((dp[i - j * j] for j in range(1, int(math.sqrt(i)) + 1) if i >= j * j))
        return dp[-1]
