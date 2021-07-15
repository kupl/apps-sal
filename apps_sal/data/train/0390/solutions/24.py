import functools

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @functools.lru_cache(maxsize = None)
        def dfs(remaining: int) -> bool:
            if remaining == 0:
                return False
            else:
                sqroot: int = int(remaining ** 0.5)
                for i in range(1, sqroot + 1):
                    if dfs(remaining - i * i):
                        continue
                    else:
                        return True
                return False
        
        return dfs(n)
