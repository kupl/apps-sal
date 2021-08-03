class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dice = [k for k in range(1, f + 1)]
        dp = [[0 for _ in range(d + 1)]for _ in range(target + 1)]

        def numRolls(d, f, target):
            for j in range(1, min(f + 1, target + 1)):
                dp[j][1] = 1
            for i in range(2, d + 1):
                for j in range(1, target + 1):
                    for new_t in list([j - k for k in dice]):
                        if new_t >= 0:
                            dp[j][i] += dp[new_t][i - 1]
                        dp[j][i] %= (10**9 + 7)
            return dp[target][d]

        return numRolls(d, f, target)

    # def numRollsToTarget(self, d: int, f: int, target: int) -> int:
    #     if d*f < target: return 0        # Handle special case, it speed things up, but not necessary
    #     elif d*f == target: return 1     # Handle special case, it speed things up, but not necessary
    #     mod = int(10**9 + 7)
    #     dp = [[0] * (target+1) for _ in range(d+1)]
    #     for j in range(1, min(f+1, target+1)): dp[1][j] = 1
    #     for i in range(2, d+1):
    #         for j in range(1, target+1):
    #             for k in range(1, f+1):
    #                 if j - k >= 0: dp[i][j] += dp[i-1][j-k]
    #             dp[i][j] %= mod
    #     return dp[-1][-1]
