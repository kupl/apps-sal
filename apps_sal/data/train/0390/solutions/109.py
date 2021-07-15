class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        @lru_cache(maxsize=None)
        def dfs(r):
          s = int(sqrt(r))
          if s**2 == r: return True
          for i in range(1, s+1):
            if not dfs(r - i **2): return True
          
          return False  # There is no i such that removing i**2 stones will win the game
          
        return dfs(n)

