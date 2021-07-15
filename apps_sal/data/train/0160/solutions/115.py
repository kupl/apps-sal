class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        
        @lru_cache(None)
        # dp(i, j) max net score alex can get
        def dp(i, j):
            if i > j:
                return 0
            if (n - j + i) % 2 == 1: # alex plays
                return max(piles[i] + dp(i + 1, j), piles[j] + dp(i, j - 1))
            return min(dp(i + 1, j) - piles[i], dp(i, j - 1) - piles[j])
        return dp(0, n - 1) > 0

