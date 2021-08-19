mod_ = 10 ** 9 + 7


class Solution:

    def countVowelPermutation(self, n: int) -> int:
        dp = [[0 for char in range(5)] for t in range(n)]
        dp[0] = [1 for char in range(5)]
        for i in range(1, n):
            dp[i][0] = (dp[i][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]) % mod_
            dp[i][1] = (dp[i][1] + dp[i - 1][0] + dp[i - 1][2]) % mod_
            dp[i][2] = (dp[i][2] + dp[i - 1][1] + dp[i - 1][3]) % mod_
            dp[i][3] = (dp[i][3] + dp[i - 1][2]) % mod_
            dp[i][4] = (dp[i][4] + dp[i - 1][2] + dp[i - 1][3]) % mod_
        return sum(dp[-1]) % mod_
