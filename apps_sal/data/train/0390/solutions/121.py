
import functools
from math import sqrt
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @functools.lru_cache(maxsize=10**5)
        def WSG(k):
            if k == 0:
                return False

            i = int(sqrt(k))
            while i >= 1:
                if not WSG(k-i**2):
                    return True
                i -= 1
            return False
        return WSG(n)
