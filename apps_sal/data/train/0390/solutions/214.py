class Solution:
    @lru_cache(None)
    def winnerSquareGame(self, n: int) -> bool:
        for i in reversed(range(1, int(sqrt(n)) + 1)):
            if not self.winnerSquareGame(n - i * i):
                return True
        return False
