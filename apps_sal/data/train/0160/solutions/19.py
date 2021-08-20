class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        @lru_cache(None)
        def solve(i, j):
            if i > j:
                return 0
            if (i + j) % 2 == 1:
                return max(solve(i + 1, j) + piles[i], solve(i, j - 1) + piles[j])
            else:
                return min(solve(i + 1, j) + piles[i], solve(i, j - 1) + piles[j])
        return solve(0, n - 1) > 0
