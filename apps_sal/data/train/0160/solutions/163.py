from functools import lru_cache


class Solution:
    def stoneGame(self, piles):
        grid = [[0] * len(piles) for x in range(len(piles))]
        for i in range(len(piles) - 1, -1, -1):
            for j in range(len(piles)):
                if i >= j:
                    grid[i][j] = 0
                else:
                    if (j - i) % 2 == 1:
                        grid[i][j] = max(piles[i] + grid[i + 1][j], piles[j] + grid[i][j - 1])
                    else:
                        grid[i][j] = min(-piles[i] + grid[i + 1][j], -piles[j] + grid[i][j - 1])
        return grid[0][len(piles) - 1] > 0
