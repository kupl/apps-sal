class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        from functools import lru_cache
        @lru_cache(None)
        def dp(i):
            if i == 0:
                return False
            if i == 1:
                return True
            for k in range(1, i+1):
                if k * k <= i:
                    if not dp(i-k*k):
                        return True
                else:
                    break
            return False
        return dp(n)
