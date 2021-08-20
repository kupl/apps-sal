class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        square = []
        for i in range(1, n + 1):
            if i * i <= n:
                square.append(i * i)
            else:
                break
        from functools import lru_cache

        @lru_cache(None)
        def dp(n, state):
            if n == 0:
                if state == 1:
                    return False
                else:
                    return True
            if state == 1:
                tmp = False
                for num in square:
                    if num <= n:
                        tmp = tmp or dp(n - num, 1 - state)
                        if tmp == True:
                            return tmp
                    else:
                        break
            else:
                tmp = True
                for num in square:
                    if num <= n:
                        tmp = tmp and dp(n - num, 1 - state)
                        if tmp == False:
                            return tmp
                    else:
                        break
            return tmp
        return dp(n, 1)
