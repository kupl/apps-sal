import functools
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        @functools.lru_cache(None)
        def helper(idx, curr):
            if curr > target: return 0
            if idx == d:
                return int(curr == target)
            res = 0
            for num in range(1, f + 1):
                res += helper(idx + 1, curr + num)
            return res % (10 ** 9 + 7)
        return helper(0, 0)
