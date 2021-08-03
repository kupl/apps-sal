class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        dp = {}

        def dfs(i, target):
            if i in dp and target in dp[i]:
                return dp[i][target]
            if target == 0:
                return 0
            if i >= 32:
                return float('inf')
            div = x ** i
            res = target % div
            ret = min(dfs(i + 1, target - res) + res * x // div * (i - 1),
                      dfs(i + 1, target - res + div) + (div - res) * x // div * (i - 1))
            if res == 0:
                ret = min(ret, target // div * i)
            dp[i] = dp.get(i, {})
            dp[i][target] = ret
            return ret
        res = target % x
        return min(dfs(2, target - res) + res * 2, dfs(2, target - res + x) + (x - res) * 2) - 1
