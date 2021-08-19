class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for i in range(target + 1)] for j in range(d)]
        print(dp)
        for i in range(f):
            if i + 1 <= target:
                dp[0][i + 1] = 1

        for i in range(1, d):
            for j in range(1, target + 1):
                # start with k = 1, accumulate all possible number sum before f
                # if this dice presents 1, then the sum up to the current j is related to the result in j-k, the previous sum in i-1 try.

                k = 1
                while j - k > 0 and k <= f:

                    dp[i][j] += dp[i - 1][j - k]
                    k += 1

        return dp[-1][-1] % (1000000000 + 7)
