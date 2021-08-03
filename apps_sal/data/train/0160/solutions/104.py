class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        self.f_map, self.s_map = dict(), dict()
        _sum = sum(piles)
        alex = self.f(piles, 0, len(piles) - 1)
        return alex > _sum / 2

    def f(self, piles, start, end):
        if start == end:
            return piles[start]
        if ((start, end) not in self.f_map):
            v_val = max(piles[start] + self.s(piles, start + 1, end), piles[end] + self.s(piles, start, end - 1))
            self.f_map[(start, end)] = v_val
        return self.f_map[(start, end)]

    def s(self, piles, start, end):
        if start == end:
            return piles[start]
        if ((start, end) not in self.s_map):
            v_val = max(piles[start] + self.f(piles, start + 1, end), piles[end] + self.f(piles, start, end - 1))
            self.s_map[(start, end)] = v_val
        return self.s_map[(start, end)]
