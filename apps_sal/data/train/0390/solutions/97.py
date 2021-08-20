import math


class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        dp = [False for _ in range(n + 1)]
        dp[1] = True
        for i in range(2, n + 1):
            sqr = int(i ** 0.5)
            for j in range(1, sqr + 1):
                dp[i] |= not dp[i - j ** 2]
                if dp[i]:
                    break
        return dp[n]
