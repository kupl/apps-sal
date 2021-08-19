class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            for x in range(1, int(sqrt(i)) + 1):
                if not dp[i - x * x]:
                    dp[i] = True
                    break
        return dp[n]
