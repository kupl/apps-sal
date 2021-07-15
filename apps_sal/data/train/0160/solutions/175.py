from functools import lru_cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(maxsize=None)
        def score(l, r):
            if l == r: return piles[l]
            return max(piles[l] - score(l+1, r),
                        piles[r] - score(l, r-1))
        return score(0, len(piles)-1) > 0
