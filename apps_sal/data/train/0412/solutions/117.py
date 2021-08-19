class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # # 1-d
        # dp = [0] * (target+1)
        # for i in range(1,min(f+1,target+1)):
        #     dp[i] = 1
        # for _ in range(d-1):
        #     for j in reversed(range(1,len(dp))):
        #         dp[j] = 0
        #         for num in range(1,f+1):
        #             if 0<=j-num:
        #                 dp[j] += dp[j-num]
        # return dp[-1] % (10**9 + 7)

        # 2-d
        dp = [[0] * (target + 1) for i in range(d)]
        for i in range(1, min(target + 1, f + 1)):
            dp[0][i] = 1
        for i in range(1, d):
            for j in range(1, target + 1):
                for num in range(1, f + 1):
                    if j - num >= 0:
                        dp[i][j] += dp[i - 1][j - num]
        return dp[-1][-1] % (10**9 + 7)
