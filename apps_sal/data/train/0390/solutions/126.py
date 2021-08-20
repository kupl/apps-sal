import math


class Solution:

    def winnerSquareGame(self, n: int) -> bool:

        @lru_cache(None)
        def helper(n):
            if n == 0:
                return False
            i = 1
            while i * i <= n:
                if not helper(n - i * i):
                    return True
                i += 1
            return False
        return helper(n)
