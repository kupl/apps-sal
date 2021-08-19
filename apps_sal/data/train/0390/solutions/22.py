import math


class Solution:

    def winnerSquareGame(self, n: int) -> bool:

        @lru_cache(None)
        def canWin(n):
            bound = math.ceil(math.sqrt(n))
            if bound * bound == n:
                return True
            for i in range(1, bound):
                if not canWin(n - i * i):
                    return True
            return False
        return canWin(n)
