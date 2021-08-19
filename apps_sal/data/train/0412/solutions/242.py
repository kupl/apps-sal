MODULE = 10**9 + 7


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target < d:
            return 0
        # 用 j 个数来凑出和为 j 的全部组合可能性
        dp = [[0] * (target + 1) for _ in range(d + 1)]
        for i in range(1, f + 1):
            if i > target:
                break
            dp[1][i] = 1

        for i in range(1, d + 1):
            for j in range(1, target + 1):
                for face in range(1, f + 1):
                    if j >= face:
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - face]) % MODULE
        # print (dp)
        return dp[d][target]
