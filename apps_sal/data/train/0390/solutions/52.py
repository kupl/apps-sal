class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(None)
        def dfs(n: int) -> bool:
            if n == 0:
                return False
            if n == 1:
                return True
            k = 1
            while (k * k) <= n:
                if not dfs(n - (k*k)):
                    return True
                k += 1
            return False
        return dfs(n)
