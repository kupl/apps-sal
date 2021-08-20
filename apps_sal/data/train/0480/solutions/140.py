class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        l = min(steps, arrLen)
        dp = [0] * l
        dp[0] = 1
        for i in range(steps):
            nextdp = [0] * l
            for j in range(l):
                if j - 1 >= 0:
                    nextdp[j] += dp[j - 1]
                nextdp[j] += dp[j]
                if j + 1 < l:
                    nextdp[j] += dp[j + 1]
                nextdp[j] %= 10 ** 9 + 7
            dp = nextdp
        return dp[0] % (10 ** 9 + 7)
