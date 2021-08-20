class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        self.sols = {}
        self.sols[d, f, target] = self.iter(d, f, target)
        return self.sols[d, f, target] % (10 ** 9 + 7)

    def iter(self, d, f, target):
        if d == 0:
            return 1 if target == 0 else 0
        if (d, f, target) in self.sols:
            return self.sols[d, f, target]
        self.sols[d, f, target] = sum([self.iter(d - 1, f, target - i) for i in range(1, f + 1)])
        return self.sols[d, f, target]
