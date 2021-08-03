class Solution:
    @lru_cache(None)
    def winnerSquareGame(self, n: int) -> bool:
        if n == 1:
            return True
        return any(not self.winnerSquareGame(n - i ** 2) for i in range(int(n ** 0.5), 0, -1))
