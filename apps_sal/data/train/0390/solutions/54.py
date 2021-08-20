class Solution:

    def winnerSquareGame(self, n: int) -> bool:

        @lru_cache(None)
        def win(n):
            if n == 1:
                return True
            if n == 0:
                return False
            v = 1
            while v * v <= n:
                if not win(n - v * v):
                    return True
                v += 1
            return False
        return win(n)
