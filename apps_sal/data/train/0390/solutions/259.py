class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        dp = [False] * (n + 1)
        for i in range(n + 1):
            for j in range(1, i + 1):
                if j * j > i:
                    break
                elif not dp[i - j * j]:
                    dp[i] = True
                    break
        return dp[n]
