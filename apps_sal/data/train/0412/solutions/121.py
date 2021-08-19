class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d > target or (d == 1 and target > f):
            return 0
        if d == target or d == 1:
            return 1
        dp = [[0 for i in range(target + 1)] for j in range(2)]
        dp_1 = [0 for i in range(target + 1)]
        for i in range(1, min(target + 1, f + 1)):
            dp_1[i] = 1
        dp[0] = dp_1
        for i in range(2, d + 1):
            dp[1] = [0 for i in range(target + 1)]
            for j in range(i, target + 1):
                if i == j:
                    dp[1][j] = 1
                    continue
                for k in range(1, min(j + 1, f + 1)):
                    dp[1][j] += dp[0][j - k] * dp_1[k]
            dp[0] = dp[1]
        return dp[1][-1] % 1000000007
