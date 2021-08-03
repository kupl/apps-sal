class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for i in range(target + 1)] for j in range(d + 1)]
        for i in range(1, d + 1):
            for j in range(1, target + 1):
                if i == 1:
                    for k in range(1, min(f + 1, target + 1)):
                        dp[i][k] = 1
                else:
                    num_permutations = 0
                    for k in range(1, f + 1):
                        if j - k >= 0:
                            num_permutations += dp[i - 1][j - k]
                    dp[i][j] = num_permutations
        return int(dp[d][target] % (10**9 + 7))
