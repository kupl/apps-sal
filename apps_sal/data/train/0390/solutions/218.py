from functools import lru_cache
class Solution:
    @lru_cache(None)
    def winnerSquareGame(self, n: int) -> bool:
        k = int(math.sqrt(n))
        if k*k ==n or n==3:
            return True
        if n==2:
            return False
        if all(self.winnerSquareGame(n-i**2) for i in range(k,0,-1)):
            return False
        return True
        
        

