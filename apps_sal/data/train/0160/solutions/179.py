from functools import lru_cache


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(None)
        def helper(l, r):
            if r - l == 1:
                return piles[l]
            if r - l == 2:
                return abs(piles[l] - piles[l + 1])
            return max(piles[l] - helper(l + 1, r), piles[r - 1] - helper(l, r - 1))

        return helper(0, len(piles)) > 0
