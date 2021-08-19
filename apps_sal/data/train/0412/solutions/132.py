class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # dp[i][j]: 用i个骰子扔出和为j的方法总数
        dp = [[0] * (target + 1) for _ in range(d + 1)]
        m = 10**9 + 7
        dp[0][0] = 1  # 由于每个骰子必选，dp[i][0], i != 0的意思是，前i个骰子都不选，是不可以的，所以为0
        for i in range(1, d + 1):
            for j in range(i, target - d + i + 1):  # 由于后面有d-j个骰子，所以我们前i个不用扔满target
                for k in range(1, min(j, f) + 1):  # 只可能扔到j，如果f超过了j，我们不要
                    dp[i][j] += dp[i - 1][j - k] % m

        return dp[d][target] % m
