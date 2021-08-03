class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        kmod = pow(10, 9) + 7
        arrLen = min(steps, arrLen)
        dp = [0] * arrLen
        dp[0] = 1

        for s in range(steps):
            tmp = [0] * arrLen
            for i in range(arrLen):
                tmp[i] = dp[i]
                if i > 0:
                    tmp[i] += dp[i - 1]
                if i < arrLen - 1:
                    tmp[i] += dp[i + 1]
                tmp[i] %= kmod
            dp = list(tmp)
        return dp[0]
