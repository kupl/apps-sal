class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}

        Alex = self.firstscore(0, len(piles), memo, piles)
        Lee = sum(piles) - Alex
        return Alex > Lee

    def firstscore(self, i, j, memo, piles):
        if i >= j:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        res = max(
            piles[i] + min(
                self.firstscore(i + 2, j, memo, piles),
                self.firstscore(i + 1, j - 1, memo, piles)
            ),
            piles[j - 1] + min(
                self.firstscore(i, j - 2, memo, piles),
                self.firstscore(i + 1, j - 1, memo, piles)
            )
        )

        memo[(i, j)] = res
        return res
