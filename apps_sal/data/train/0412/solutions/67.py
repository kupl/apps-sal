class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # f(n) = f(n - 1) + f(n-2) + ...
        dp = [[0 for i in range(target+1)] for t in range(d+1)]
        for dd in range(1, d+1):
            for tt in range(dd, min(f*dd, target)+1):
                if dd == 1:
                    dp[dd][tt] = 1
                else:
                    end = tt -1
                    start = max(1, tt-f)
                    dp[dd][tt] = sum(dp[dd-1][start:end+1])
        return dp[d][target]%(10**9 + 7)
        
    

