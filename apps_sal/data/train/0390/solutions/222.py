from math import sqrt


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        from functools import lru_cache

        @lru_cache(None)
        def df(x):
            if int(sqrt(x)) ** 2 == x:
                return True
            if not x:
                return False
            for i in range(int(sqrt(x)), 0, -1):
                if not df(x - i * i):
                    return True
            return False
        return df(n)
