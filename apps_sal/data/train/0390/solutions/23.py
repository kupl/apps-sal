class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(maxsize=None)
        def helper(i):
            if i == 0:
                return False
            sr = int(i**0.5)
            for k in range(1, sr + 1):
                if not helper(i - k * k):
                    return True
            return False

        return helper(n)
