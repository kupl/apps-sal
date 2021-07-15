class Solution:
    @lru_cache(None)
    def winnerSquareGame(self, n: int) -> bool:
        return True if n == 1 else any(not self.winnerSquareGame(n - i ** 2) for i in range(int(n ** 0.5), 0, -1))
               
            
            

