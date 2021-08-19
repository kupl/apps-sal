class Solution:

    def __init__(self):
        self.g = []

    def recurse(self, piles, i, j):
        if self.g[i][j]:
            return self.g[i][j]
        if j - i <= 1:
            return True
        self.g[i][j] = self.recurse(piles, i + 1, j) or self.recurse(piles, i, j - 1)
        return self.g[i][j]

    def stoneGame(self, piles: List[int]) -> bool:
        if not piles:
            return True
        self.g = [[False] * len(piles) for i in range(len(piles))]
        ans = self.recurse(piles, 0, len(piles) - 1)
        return ans
