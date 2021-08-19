from functools import lru_cache


class Solution:

    def stoneGame(self, piles: List[int]) -> bool:

        @lru_cache(None)
        def dp(i, j):
            if i > j:
                return 0
            term = (j - i) % 2
            if term == 1:
                return max(dp(i + 1, j) + piles[i], dp(i, j - 1) + piles[j])
            else:
                return min(dp(i + 1, j) - piles[i], dp(i, j - 1) - piles[j])
        return dp(0, len(piles) - 1) > 0
