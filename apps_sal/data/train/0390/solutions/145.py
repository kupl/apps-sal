class Solution:

    @lru_cache(None)
    def winnerSquareGame(self, n: int) -> bool:
        if n == 0:
            return False
        for i in range(1, int(n ** 0.5) + 1):
            if not self.winnerSquareGame(n - i ** 2):
                return True
        return False
