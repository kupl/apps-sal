class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for _ in range(target + 1)] for _ in range(d + 1)]
        dp[0][0] = 1
        for i in range(1, d + 1):
            for j in range(i * 1, min(target + 1, i * f + 1)):
                for r in range(1, f + 1):
                    if j - r >= 0:
                        dp[i][j] += dp[i - 1][j - r]
        return dp[-1][-1] % (10**9 + 7)

        self.res = 0

        def dfs(dice, sum):
            for i in range(1, f + 1):
                if dice == d:
                    if sum + i == target:
                        self.res += 1
                elif sum + i < target:
                    dfs(dice + 1, sum + i)
        dfs(1, 0)
        return self.res
