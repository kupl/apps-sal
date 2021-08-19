class Solution:

    def stoneGame(self, piles: List[int]) -> bool:

        @lru_cache(None)
        def get_score(i, j):
            if i > j:
                return 0
            if i == j:
                return piles[i]
            return max(piles[i] + get_score(i + 2, j), piles[i] + get_score(i + 1, j - 1), piles[j] + get_score(i + 1, j - 1), piles[j] + get_score(i, j - 2))
        return 2 * get_score(0, len(piles) - 1) > sum(piles)
