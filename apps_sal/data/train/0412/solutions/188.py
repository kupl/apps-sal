class Solution:

    def numRollsToTarget(self, d: int, f: int, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        temp = [0 for i in range(n + 1)]
        lol = [0 for i in range(n + 1)]
        for i in range(1, d + 1):
            for j in range(i, n + 1):
                for k in range(1, min(f + 1, j + 1)):
                    temp[j] += dp[j - k]
                    temp[j] = temp[j] % mod
            dp = temp.copy()
            temp = lol.copy()
        return dp[-1]
