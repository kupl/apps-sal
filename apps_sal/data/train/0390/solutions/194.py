class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        for i in range(1, len(dp)):
            j = 1
            while j * j <= i:
                if dp[i - j * j] == False:
                    dp[i] = True
                j += 1
        return dp[-1]
