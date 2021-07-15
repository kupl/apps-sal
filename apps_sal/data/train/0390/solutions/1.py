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
    
    # def winnerSquareGame(self, n: int) -> bool:
    #     result = [None] * (n + 1)
    #     def canWin(n):
    #         bound = math.ceil(math.sqrt(n))
    #         if bound * bound == n:
    #             result[n] = True
    #             return True
    #         if result[n] != None:
    #             return result[n]
    #         for i in range(1, bound):
    #             if not canWin(n - i * i):
    #                 result[n] = True
    #                 return True
    #         result[n] = False
    #         return False
    #     return canWin(n)

