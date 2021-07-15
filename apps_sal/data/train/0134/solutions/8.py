from functools import lru_cache
class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        @lru_cache(None)
        def dfs(state, x, lz=False):
            n = len(str(x))
            if x < 10:
                res = 0
                if not lz:
                    for i in range(1, x + 1):
                        if state & (1 << i) == 0:
                            res += 1
                else:
                    for i in range(x + 1):
                        if state & (1 << i) == 0:
                            res += 1
                # print(bin(state), x, lz, res)
                return res
            if not lz:
                res = dfs(state, 10 ** (n - 1) - 1)
            else:
                if state & 1 == 0:
                    res = dfs(state | 1, 10 ** (n - 1) - 1, True)
                else:
                    res = 0
            for i in range(1, int(str(x)[0])):
                if state & (1 << i) == 0:
                    res += dfs(state | (1 << i), 10 ** (n - 1) - 1, True)
            if state & (1 << int(str(x)[0])) == 0:
                if not (x % 10 ** (n - 1) == 0 and n >= 3):
                    if x % 10 ** (n - 1) >= 10 ** (n - 2) or n <= 2:
                        res += dfs(state | (1 << int(str(x)[0])), x % 10 ** (n - 1), True)
                    elif n >= 3 and 1 & state == 0 and x % 10 ** (n - 1) >= 10 ** (n - 3):
                        res += dfs(state | (1 << int(str(x)[0])) + 1, x % 10 ** (n - 1), True)
            # print(bin(state), x, lz, res)
            return res
        
        return N - dfs(0, N)

