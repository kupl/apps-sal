from functools import lru_cache

class Solution:
    
    @lru_cache(None)
    def dp(self, n):
        if n == 0:
            return False
        for s in self.s:
            if n-s >= 0:
                if not self.dp(n-s):
                    return True
        return False
        
    
    def winnerSquareGame(self, n: int) -> bool:
        self.s, i = [1], 1
        while self.s[-1] < 10**5:
            i += 1
            self.s.append(i*i)
        
        return self.dp(n)

