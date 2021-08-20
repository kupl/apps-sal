class Solution:

    def winnerSquareGame(self, n: int) -> bool:

        @lru_cache(None)
        def helper(i):
            if i in [0, 2]:
                return False
            base = int(i ** 0.5)
            if base * base == i:
                return True
            return any((not helper(i - j * j) for j in range(base, 0, -1)))
        return helper(n)
