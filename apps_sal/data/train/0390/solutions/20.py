 
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(maxsize=None)
        def dfs(n):
            if n == 0:
                return False
            square_root = int(sqrt(n))
            for i in range(1, square_root + 1):
                if not dfs(n - i * i):
                    return True
            return False                  
        return dfs(n)

