from functools import lru_cache


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:

        if d * f < target:
            return 0

        @lru_cache(maxsize=None)
        def dfs(index, target):
            if index == d:
                if target == 0:
                    return 1
                return 0

            if target <= 0:
                return 0

            ret = [0] * (f + 1)
            for num in range(1, f + 1):
                ret[num] = dfs(index + 1, target - num)

            return sum(ret) % (10**9 + 7)

        return dfs(0, target)
