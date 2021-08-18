class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        @lru_cache(None)
        def helper(n):
            if n == 0:
                return 0
            i = 1
            sq = 1
            while sq <= n:
                if helper(n - sq) == 0:
                    return 1
                i += 1
                sq = i * i
            return 0

        return helper(n)
