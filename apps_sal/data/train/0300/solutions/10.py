from functools import lru_cache


class Solution:

    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        cost = list(range(40))
        cost[0] = 2

        @lru_cache(None)
        def dp(i, targ):
            if targ == 0:
                return 0
            if targ == 1:
                return cost[i]
            if i >= 39:
                return float('inf')
            (t, r) = divmod(targ, x)
            return min(r * cost[i] + dp(i + 1, t), (x - r) * cost[i] + dp(i + 1, t + 1))
        return dp(0, target) - 1
