class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        dp = {}
        def dfs(steps, ind):
            if (steps, ind) in dp:
                return dp[(steps, ind)]
            if steps == ind:
                return 1
            elif steps == 0:
                return 0
            res = 0
            res += dfs(steps-1, ind)
            if ind > 0:
                res += dfs(steps-1, ind-1)
            if ind < arrLen-1:
                res += dfs(steps-1, ind+1)
            dp[(steps, ind)] = res
            return res%(10**9+7)
        return dfs(steps, 0)
