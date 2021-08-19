from functools import lru_cache


class Solution:

    def winnerSquareGame(self, n: int) -> bool:

        @lru_cache(None)
        def dp(k):
            if k == 1:
                return True
            if k == 0:
                return False
            for i in range(1, k):
                if i * i > k:
                    break
                if not dp(k - i * i):
                    return True
            return False
        return dp(n)
