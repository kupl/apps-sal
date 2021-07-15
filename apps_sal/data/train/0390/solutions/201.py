class Solution:
    @lru_cache(None)
    def winnerSquareGame(self, n: int) -> bool:
        if n == 0 or n == 1: return True
        i = int(sqrt(n))
        if i ** 2 == n: return True
        while i > 0:
            if not self.winnerSquareGame(n - i ** 2): return True
            i -= 1
        return False
