# from (D * F * target) -> O(D * target)
class Solution:
    def numRollsToTarget(self, D: int, F: int, target: int) -> int:
        # dp[d][t] -> how many ways to form t using d dices
        dp = [[0] * (target + 1) for _ in range(2)]
        dp[0][0] = 1
        for d in range(1, D + 1):
            cd = d & 0x1
            pd = (d - 1) & 0x1
            dp[cd][0] = 0
            for t in range(1, target + 1):
                dp[cd][t] = (dp[cd][t - 1] + dp[pd][t - 1] - (dp[pd][t - F - 1] if t - F - 1 >= 0 else 0)) % 1000000007
        return dp[D & 0x1][target]
    
    def numRollsToTarget(self, D: int, F: int, target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for d in range(1, D + 1):
            ndp = [0] * (target + 1)
            for i in range(1, target + 1):    
                ndp[i] = sum(dp[i - f] for f in range(1, F + 1) if i - f >= 0) % 1000000007
            dp = ndp
        return dp[-1]
