import math
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        result = dict()
        def canWin(n):
            bound = math.ceil(math.sqrt(n))
            if n in result:
                return result[n]
            result[n] = False
            for i in range(1, bound + 1):
                if n == i * i:
                    result[n] = True
                    return True
                if n > i * i:
                    if not canWin(n - i * i):
                        result[n] = True
                        return True
            return result[n]
        return canWin(n)
