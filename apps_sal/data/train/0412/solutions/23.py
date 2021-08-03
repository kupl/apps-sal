class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}

        def dp(d, target):
            nonlocal memo, f
            if d == 0:
                return 1 if target == 0 else 0
            if (d, target) in memo:
                return memo[(d, target)]
            res = 0
            for i in range(max(0, target - f), target):
                res += dp(d - 1, i)
            memo[(d, target)] = res
            return res
        return dp(d, target) % (10**9 + 7)
