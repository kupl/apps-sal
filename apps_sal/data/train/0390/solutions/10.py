class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        dp = [0 for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                if j * j > i:
                    break
                if dp[i - j * j] == 0:
                    dp[i] = 1
                    break
        return dp[-1]
