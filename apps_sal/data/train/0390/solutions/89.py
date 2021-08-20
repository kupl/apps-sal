class Solution:

    @lru_cache(None)
    def winnerSquareGame(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        xsqrt = int(n ** 0.5) + 1
        for i in range(1, xsqrt):
            if not self.winnerSquareGame(n - i * i):
                return True
        return False
