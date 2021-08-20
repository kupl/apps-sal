class Solution:

    @lru_cache(None)
    def winnerSquareGame(self, n: int) -> bool:
        if n == 0:
            return False
        return any((not self.winnerSquareGame(n - x ** 2) for x in range(int(n ** 0.5), 0, -1)))
