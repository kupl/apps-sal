class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)

        for i in range(1, n + 1):
            for j in range(1, int(math.sqrt(i)) + 1):
                if dp[i - j * j] == False:
                    dp[i] = True
                    break

        return dp[-1]
