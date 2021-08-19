class Solution:
    @lru_cache(maxsize=None)
    def winnerSquareGame(self, n: int) -> bool:
        # if a perfect square is available, you win
        if int(sqrt(n)) ** 2 == n:
            return True

        for i in range(1, int(sqrt(n)) + 1):
            if not self.winnerSquareGame(n - i * i):
                return True

        return False
