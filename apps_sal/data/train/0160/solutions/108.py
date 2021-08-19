class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {}

        def firstscore(i, j):
            if i >= j:
                return 0
            # if j == i+1 and j < len(piles): #because [i, j)
            #     return piles[i]
            if (i, j) in cache:
                return cache[i, j]
            res = max(piles[i] + min(firstscore(i + 2, j), firstscore(i + 1, j - 1)),
                      piles[j - 1] + min(firstscore(i + 1, j - 1), firstscore(i, j - 2)))
            cache[i, j] = res
            return cache[i, j]
        Alex = firstscore(0, len(piles))
        Lee = sum(piles) - Alex
        return Alex > Lee
