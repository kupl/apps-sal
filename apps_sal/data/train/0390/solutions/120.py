from functools import lru_cache

class Solution:
    @lru_cache(None)
    def winnerSquareGame(self, n: int) -> bool:
        if n == 0:
            return False
        x = 1
        while x*x <= n:
            if not self.winnerSquareGame(n-x*x):
                return True
            x += 1
        return False

