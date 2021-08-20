class Solution:

    def winnerSquareGame(self, n: int) -> bool:

        @lru_cache(None)
        def helper(n):
            if n == 0:
                return -1
            for i in range(int(sqrt(n)), 0, -1):
                if helper(n - i * i) < 0:
                    return 1
            return -1
        return helper(n) > 0
