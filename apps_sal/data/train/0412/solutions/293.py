class Solution:

    MODULO = 10**9 + 7
    table = {}

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        return self.recursive(d, f, target) % self.MODULO

    def recursive(self, d: int, f: int, target: int):
        if target < d or target > d * f:
            return 0
        if d == 1 and target <= f:
            return 1
        sum_ = 0
        for i in range(1, f + 1):
            idx = (d - 1, f, target - i)
            if idx not in self.table:
                self.table[idx] = self.recursive(*idx)
            sum_ += self.table[idx] % self.MODULO
        return sum_
