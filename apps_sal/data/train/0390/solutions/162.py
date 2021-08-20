import math


class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        result = dict()

        def canWin(n):
            bound = math.ceil(math.sqrt(n))
            if bound * bound == n:
                result[n] = True
                return True
            if n in result:
                return result[n]
            for i in range(1, bound):
                if not canWin(n - i * i):
                    result[n] = True
                    return True
            result[n] = False
            return False
        return canWin(n)
