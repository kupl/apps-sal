class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(None)
        def dfs(m, p):
            if m == 0:
                #print(m, p, p == 1)
                return p == 1
            if m == 1:
                #print(m, p, p == 0)
                return p == 0
            i = 1
            while i * i <= m:
                if p == 0 and dfs(m - i * i, 1):
                    #print(m, p, True)
                    return True
                elif p == 1 and not dfs(m - i * i, 0):
                    #print(m, p, False)
                    return False
                i += 1
            #print(m, p, p == 1)
            return p == 1
        return dfs(n, 0)
