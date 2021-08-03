from functools import lru_cache


class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        @lru_cache(None)
        def dp(m):
            if m == 0:
                return True
            if int(math.sqrt(m)) ** 2 == m:
                return True

            i = 1
            while i * i <= m:
                if not dp(m - i * i):
                    return True
                i += 1

            return False

        return dp(n)
