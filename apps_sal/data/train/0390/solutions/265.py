from functools import lru_cache


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [None] * (n + 1)
        dp[0] = False
        i = 1
        while i ** 2 <= n:
            dp[i**2] = True
            i += 1
        sq = 1
        for i in range(2, n + 1):
            if dp[i]:
                continue

            dp[i] = False
            sq = int(math.sqrt(i))
            for k in range(sq, 0, -1):
                if not dp[i - k**2]:
                    dp[i] = True
                    break

        return dp[n]
