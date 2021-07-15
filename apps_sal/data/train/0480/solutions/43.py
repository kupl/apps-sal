class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10 ** 9 + 7
        memo = {}
        def dfs(steps, i):
            if not steps:
                return int(i == 0)
            
            if (steps, i) in memo:
                return memo[(steps, i)]
            
            res = dfs(steps - 1, i)
            if i - 1 >= 0:
                res += dfs(steps - 1, i - 1)
            
            if i + 1 <= arrLen - 1:
                res += dfs(steps - 1, i + 1)
            
            memo[(steps, i)] = res % mod
            return memo[(steps, i)]
        
        return dfs(steps, 0)

