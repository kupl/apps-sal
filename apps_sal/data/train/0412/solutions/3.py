class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # dp[d][target] = sum(dp[d-1][target - w]) w in 1-f
        dp = {0: 1}
        MOD = 10 ** 9 + 7
        for i in range(d):
            ndp = {}
            for k, v in list(dp.items()):
                for w in range(1, f+1):
                    if k + w <= target: 
                        ndp[k+w] = (ndp.get(k+w, 0) + dp[k] ) % MOD
            dp = ndp.copy()
        return dp.get(target, 0)

