class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        i = 0
        j = len(piles) - 1
        self.memo = {}
        score = self.recurse(piles, i, j, True)
        return score > 0

    def recurse(self, piles, i, j, a_turn):
        if (i, j) in self.memo:
            return self.memo[i, j]
        if i == j:
            return 0
        if a_turn:
            l = self.recurse(piles, i + 1, j, False) + piles[i]
            r = self.recurse(piles, i, j - 1, False) + piles[j]
            self.memo[i, j] = max(l, r)
        else:
            l = self.recurse(piles, i + 1, j, True) - piles[i]
            r = self.recurse(piles, i, j - 1, True) - piles[j]
            self.memo[i, j] = min(l, r)
        return self.memo[i, j]
