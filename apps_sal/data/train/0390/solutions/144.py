class Solution:

    def winnerSquareGame(self, n: int) -> bool:

        @lru_cache(None)
        def rec(n):
            if n < 2:
                return n == 1
            return any((not rec(n - i * i) for i in range(int(n ** 0.5), 0, -1)))
        return rec(n)
