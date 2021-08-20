class Solution:

    def __init__(self):
        self.memo = {}

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d * f < target:
            return 0
        if d == 1:
            return 1
        if (d, target) in self.memo:
            return self.memo[d, target]
        numWays = 0
        for i in range(f, 0, -1):
            if target - i > 0:
                ways = self.memo.get((d - 1, target - i), self.numRollsToTarget(d - 1, f, target - i))
                numWays += ways
        self.memo[d, target] = numWays
        return numWays % (10 ** 9 + 7)
