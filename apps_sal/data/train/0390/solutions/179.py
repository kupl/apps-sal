class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        @lru_cache(None)
        def test(n):
            if n == 0:
                return False

            for i in range(1, int(n ** 0.5) + 1):
                sn = i ** 2
                if not test(n - sn):
                    return True

            return False

        return test(n)
