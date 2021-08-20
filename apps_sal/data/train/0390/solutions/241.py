from functools import lru_cache


class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        sq = [x * x for x in range(1, 317)]
        dp = [False] * (n + 1)
        for i in range(n + 1):
            for x in sq:
                if i - x < 0:
                    break
                if dp[i - x] == False:
                    dp[i] = True
                    break
        return dp[n]
