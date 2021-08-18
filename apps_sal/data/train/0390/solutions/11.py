class Solution:
    @lru_cache(None)
    def winnerSquareGame(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True

        xsqrt = int(n**0.5)
        for i in range(xsqrt, 0, -1):
            if not self.winnerSquareGame(n - i * i):
                return True

        return False
