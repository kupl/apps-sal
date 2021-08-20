class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        @lru_cache(None)
        def sumRange(i, j):
            if i == j:
                return piles[i]
            else:
                return piles[i] + sumRange(i + 1, j)

        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return piles[i]
            else:
                return max(piles[i] + sumRange(i + 1, j) - dp(i + 1, j), piles[j] + sumRange(i, j - 1) - dp(i, j - 1))
        Alex = dp(0, n - 1)
        Lee = sumRange(0, n - 1) - Alex
        return Alex > Lee
