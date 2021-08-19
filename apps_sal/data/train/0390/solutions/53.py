class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * 160000
        m = 400
        for i in range(1, m):
            dp[i * i] = True
        for i in range(1, n + 1):
            for j in range(1, m):
                if i > j * j:
                    if not dp[i - j * j]:
                        dp[i] = True
                        break
                else:
                    break
        return dp[n]
