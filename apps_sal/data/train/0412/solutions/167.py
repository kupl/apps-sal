MOD = 1000000007


class Solution:
    dyn = {}

    def _get_res(self, d, f, target):
        if d == 1:
            return 1 if 0 < target and target <= f else 0
        if (d, f, target) in self.dyn:
            return self.dyn[d, f, target]
        res = 0
        for i in range(1, f + 1):
            res += self._get_res(d - 1, f, target - i)
        self.dyn[d, f, target] = res
        return res

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        return self._get_res(d, f, target) % MOD
