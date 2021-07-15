from functools import lru_cache
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(maxsize=None)
        def win(cur):
            if cur == 0: return False            
            for i in range(1, int(cur**0.5)+1):
                if not win(cur - i*i):
                    return True                
            return False
        
        return win(n)

