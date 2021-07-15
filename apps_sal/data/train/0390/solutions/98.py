class Solution:
    @lru_cache(None)
    def winnerSquareGame(self, n: int) -> bool:
        if n <= 1:
            return n == 1
        
        for i in range(1, n+1):
            sq = i*i
            if sq > n:
                break
            
            if not self.winnerSquareGame(n-sq):
                return True
        
        return False
