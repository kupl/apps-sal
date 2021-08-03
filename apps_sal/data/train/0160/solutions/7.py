class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        @lru_cache(None)
        def play(i, j, alexTurn):
            if i > j:
                return 0

            if alexTurn:
                return max(play(i + 1, j, False) + piles[i], play(i, j - 1, False) + piles[j])
            else:
                return min(play(i + 1, j, True) - piles[i], play(i, j - 1, True) - piles[j])

        return play(0, len(piles) - 1, True) > 0
