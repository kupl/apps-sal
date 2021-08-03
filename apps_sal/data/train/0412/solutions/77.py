class Solution:
    def __init__(self):
        self.memo = {}

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        res = 0
        if (d, target) in self.memo:
            return self.memo[(d, target)]
        for i in range(1, f + 1):
            if target - i == 0 and d == 1:
                res += 1
            elif target - i > 0 and d > 1:
                res += self.numRollsToTarget(d - 1, f, target - i)
        self.memo[(d, target)] = res
        return res % (10 ** 9 + 7)
