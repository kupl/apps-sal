class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        dp[0] = False
        for i in range(1, n + 1):
            k = 1
            while k**2 <= i:
                if dp[i - k**2] == False:
                    dp[i] = True
                    break
                k += 1
        return dp[n]
