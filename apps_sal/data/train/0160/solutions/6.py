class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        lp = len(piles)

        from functools import lru_cache

        @lru_cache(None)
        def dp(i, j):
            if i > j:
                return 0
            parity = (j - i) % 2
            if parity == 1:
                return max(piles[i] + dp(i + 1, j), piles[j] + dp(i, j - 1))
            if parity == 0:
                return min(-piles[i] + dp(i + 1, j), -piles[j] + dp(i, j - 1))

        return dp(0, lp - 1) > 0
