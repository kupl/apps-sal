class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        from functools import lru_cache

        @lru_cache(None)
        def dp(n):
            if math.sqrt(n) == round(math.sqrt(n)):
                return True
            i = 1
            while i**2 < n:
                if not dp(n - i**2):
                    return True
                i += 1
            return False
        return dp(n)
