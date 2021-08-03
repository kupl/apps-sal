class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        @lru_cache(None)
        def game(left, right):
            if left == right:
                return piles[left]
            return max(piles[left] - game(left + 1, right), piles[right] - game(left, right - 1))

        return game(0, len(piles) - 1) > 0
