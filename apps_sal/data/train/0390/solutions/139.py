from functools import lru_cache


class Solution:

    def winnerSquareGame(self, n: int) -> bool:

        @lru_cache(None)
        def dp(num):
            sqr = int(num ** (1 / 2))
            if sqr ** 2 == num:
                return True
            way = False
            for i in range(1, sqr + 1):
                way = not dp(num - i ** 2)
                if way:
                    return True
            return way
        return dp(n)
