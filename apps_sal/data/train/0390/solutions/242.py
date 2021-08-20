class Solution:

    def winnerSquareGame(self, n: int) -> bool:

        @lru_cache(None)
        def helper(i):
            if i == 0:
                return False
            base = int(i ** 0.5)
            return any((not helper(i - j * j) for j in range(base, 0, -1)))
        return helper(n)
