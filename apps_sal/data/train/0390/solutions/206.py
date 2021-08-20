class Solution:

    def winnerSquareGame(self, n: int) -> bool:

        @lru_cache(None)
        def get(k):
            if not k:
                return False
            return not all([get(k - i * i) for i in range(1, int(k ** 0.5) + 1)])
        return get(n)
