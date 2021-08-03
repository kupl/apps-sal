
import functools


class Solution:
    @functools.lru_cache(maxsize=None)
    def winnerSquareGame(self, n: int) -> bool:
        if n == 0:
            return False

        i = 1
        while i**2 <= n:
            if not self.winnerSquareGame(n - i**2):
                return True
            i += 1
        return False
