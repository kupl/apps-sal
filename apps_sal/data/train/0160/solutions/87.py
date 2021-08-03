class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        self.cache = {}
        self.piles = piles
        return self.minimax(0, len(piles) - 1, True) > 0

    def minimax(self, l, r, is_alex):
        if (l, r) in self.cache:
            return self.cache[(l, r)]

        if l > r:
            return 0

        piles = self.piles

        if is_alex:
            res = max(self.minimax(l + 1, r, False) + piles[l], self.minimax(l, r - 1, False) + piles[r])
            self.cache[(l, r)] = max(self.cache[(l, r)], res) if (l, r) in self.cache else res
        else:
            res = min(self.minimax(l + 1, r, True) - piles[l], self.minimax(l, r - 1, True) - piles[r])
            self.cache[(l, r)] = max(self.cache[(l, r)], res) if (l, r) in self.cache else res
        return self.cache[(l, r)]
