class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = dict()

        def fun(d, target):
            mod = int(1000000000.0 + 7)
            if target == 0 and d == 0:
                return 1
            if target == 0 and d != 0:
                return 0
            if target < 0:
                return 0
            if d == 0:
                return 0
            if (d, target) in dp:
                return dp[d, target]
            tmp = 0
            for i in range(1, f + 1):
                tmp += fun(d - 1, target - i) % mod
                tmp %= mod
            dp[d, target] = tmp
            return tmp
        return fun(d, target)
