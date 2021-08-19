class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for _ in range(max(target + 1, f + 1))] for _ in range(d + 1)]
        for i in range(1, f + 1):
            dp[1][i] = 1
        break_flag = False
        for i in range(1, d):
            break_flag = False
            for j in range(1, max(target + 1, f + 1)):
                for n in range(1, f + 1):
                    if j + n <= max(target, f):
                        dp[i + 1][j + n] += dp[i][j]
                    else:
                        break
                        break_flag = True
                if break_flag:
                    break
        return dp[d][target] % (10 ** 9 + 7)
