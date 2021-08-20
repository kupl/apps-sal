class Solution:
    cache = {}

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d == 1:
            if f < target:
                return 0
            else:
                return 1
        if (d, f, target) in self.cache:
            return self.cache[d, f, target]
        else:
            num = sum((self.numRollsToTarget(d - 1, f, target - i) for i in range(1, min(f + 1, target)))) % (10 ** 9 + 7)
            self.cache[d, f, target] = num
        return num
