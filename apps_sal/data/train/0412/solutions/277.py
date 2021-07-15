class Solution:
    def numRollsToTarget(self, d, f, target):
        if (target < d) or (target > d*f): return 0
        dp = [[0 for _ in range(d*f+1)] for _ in range(d+1)]
        for v in range(1, f+1):
            dp[1][v] = 1
        for dcnt in range(2, d+1):
            for total in range(dcnt, target+1):
                for v in range(1, f+1):
                    dp[dcnt][total] += dp[dcnt-1][total-v]
        return dp[d][target] % (10**9 + 7)
    
class Solution:
    def numRollsToTarget(self, d, f, target):
        if (target < d) or (target > d*f): return 0
        dp = [[0 for _ in range(d*f+1)] for _ in range(d+1)]
        for v in range(1, f+1):
            dp[1][v] = 1
        for dcnt in range(2, d+1):
            for total in range(dcnt, target+1):
                for v in range(1, f+1):
                    dp[dcnt][total] += dp[dcnt-1][total-v]
        return dp[d][target] % (10**9 + 7)
