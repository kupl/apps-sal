class Solution:

    @lru_cache(1024 ** 2)
    def winnerSquareGame(self, n: int) -> bool:
        if n == 0:
            return False
        for i in range(1, int(sqrt(n)) + 1):
            if i * i > n:
                continue
            if not self.winnerSquareGame(n - i * i):
                return True
        return False
