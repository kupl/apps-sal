class Solution:
    @lru_cache(None)
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d == 0 or target <= 0:
            return d == 0 and target == 0
        res = 0
        for i in range(1, f + 1):
            res = (res + self.numRollsToTarget(d - 1, f, target - i)) % (10**9 + 7)
        return res
