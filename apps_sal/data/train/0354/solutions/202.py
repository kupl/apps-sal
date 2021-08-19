class Solution:

    @lru_cache(maxsize=None)
    def roll(self, val, consec, left):
        if left == 0:
            return 1
        total = 0
        for i in range(0, 6):
            if i != val:
                total += self.roll(i, 1, left - 1)
        if consec < self.rm[val]:
            total += self.roll(val, consec + 1, left - 1)
        return total

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        self.rm = rollMax
        return self.roll(0, 0, n) % (10 ** 9 + 7)
