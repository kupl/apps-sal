class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        dp = [False] * (n + 1)
        dp[1] = True
        for i in range(1, n + 1):
            for j in range(1, i):
                if j * j > i:
                    break
                elif not dp[i - j * j]:
                    dp[i] = True
                    break
        return dp[n]
