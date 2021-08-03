class Solution:
    def __init__(self):
        self.mem = {}

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target < d or target > d * f:
            return 0
        if d == 0 or target == 0:
            return 0
        if d == 1 and target <= f:
            return 1
        key = (d, f, target)
        if key in self.mem:
            return self.mem[key]
        Sum = 0
        for i in range(1, f + 1):
            Sum += self.numRollsToTarget(d - 1, f, target - i)
            Sum %= (10**9 + 7)
        self.mem[key] = Sum
        return (self.mem[key])
