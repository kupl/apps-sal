class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        kmod = pow(10, 9) + 7
        arrLen = min(steps, arrLen)
        dp = [[0] * arrLen for _ in range(steps + 1)]
        dp[0][0] = 1
        dirs = [0, -1, 1]

        for s in range(steps):
            for i in range(arrLen):
                if dp[s][i]:
                    for d in dirs:
                        j = i + d
                        if j < 0 or j >= arrLen:
                            continue
                        dp[s + 1][j] += dp[s][i]
            for i in range(arrLen):
                dp[s + 1][i] %= kmod

        return dp[steps][0]
