class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # 2. Bottom-up Dynamic Programming
        #   DP Array where target is the column and numDices is the row

        #   Range of values:
        #   1 dice -> (1 , f)
        #   2 dices -> (2, 2f)
        #   d dices -> (d, fd)
        dp = [[0 for _ in range(target + 1)] for _ in range(d + 1)]
        dp[0][0] = 1
        for n in range(1, d + 1):
            for i in range(1 * n, min(target + 1, f * n + 1)):
                for j in range(1, f + 1):
                    if i - j >= 0:
                        dp[n][i] += dp[n - 1][i - j]
        return dp[-1][-1] % (10**9 + 7)

        # 1. Recursion: O(F^D) Time, O(F^D) Space
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
