class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        self.mapx = {}
        return self.rec(d, f, target)

    def rec(self, d, f, target):
        if d == 0:
            if target == 0:
                return 1
            return 0
        count = 0
        for num in range(1, f + 1):
            if target - num >= 0:
                nextState = (d - 1, target - num)
                if nextState not in self.mapx:
                    count += self.rec(d - 1, f, target - num)
                else:
                    count += self.mapx.get(nextState, 0)
        count = count % 1000000007
        self.mapx[d, target] = count
        return count
