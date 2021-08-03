class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:

        dp = [[0] * (target + 1) for _ in range(d)]

        l = min(target + 1, f + 1)

        for i in range(1, l):
            dp[0][i] = 1

        for level in range(1, d):

            # for face in range(1,f+1):
            for t in range(1, target + 1):

                for face in range(1, f + 1):

                    if t - face > 0:
                        dp[level][t] += dp[level - 1][t - face]

        # print(dp)
        return dp[-1][-1] % (10**9 + 7)
