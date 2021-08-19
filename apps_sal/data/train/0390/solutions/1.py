import math


class Solution:

    def winnerSquareGame(self, n: int) -> bool:

        @lru_cache(None)
        def canWin(n):
            bound = math.floor(math.sqrt(n))
            if bound * bound == n:
                return True
            for i in range(bound, 0, -1):
                if not canWin(n - i * i):
                    return True
            return False
        return canWin(n)
