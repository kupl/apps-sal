class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        self.mp = {}
        t = self.foo(0, len(piles) - 1, piles)
        return sum(piles) < 2 * t

    def foo(self, i, j, p):
        if i == j:
            return p[i]
        key = str(i) + str(j)
        if key in self.mp:
            return self.mp[key]
        v = max(p[i] + self.foo(i + 1, j, p), p[j] + self.foo(i, j - 1, p))
        self.mp[key] = v
        return v
