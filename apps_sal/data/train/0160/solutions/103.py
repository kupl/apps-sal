class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(None)
        def dp(i, j):
            if i + 1 == j:
                arr = piles[i + 1: j + 1]
                return max(arr) - min(arr)

            L, R = piles[i], piles[j]

            return max(L - R + dp(i + 1, j), R - L + dp(i, j - 1))

        return dp(0, len(piles) - 1) > 0
