class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            k = 1
            while k * k <= i:
                if dp[i - k * k] == False:
                    dp[i] = True
                    break
                k += 1
        return dp[n]
