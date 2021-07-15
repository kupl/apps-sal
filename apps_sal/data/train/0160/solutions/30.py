class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(None)
        def dp(i, j):
            if i >= j or j >= len(piles): return 0
            if i + 1 == j:
                return max(piles[i:j + 1])
            res = piles[i] + max(dp(i + 2, j), dp(i + 1, j - 1))
            res = max(res, piles[j] + max(dp(i, j - 2), dp(i + 1, j - 1)))
            return res
        return dp(0, len(piles) - 1) > sum(piles)//2

