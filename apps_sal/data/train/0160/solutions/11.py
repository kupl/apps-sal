import functools


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n: int = len(piles)

        @functools.lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            if i > j:
                return 0
            parity: int = (j - i - n) % 2
            if parity == 1:
                return max(dp(i + 1, j) + piles[i], dp(i, j - 1) + piles[j])
            else:
                return min(dp(i + 1, j) - piles[i], dp(i, j - 1) - piles[j])
        return dp(0, n - 1) > 0
