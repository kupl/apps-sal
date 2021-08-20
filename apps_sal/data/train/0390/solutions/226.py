class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        for i in range(n + 1):
            if i == int(sqrt(i)) ** 2:
                dp[i] = True
            else:
                for j in range(1, int(i ** 0.5) + 1):
                    if not dp[i - j * j]:
                        dp[i] = True
                        break
        return dp[n]
