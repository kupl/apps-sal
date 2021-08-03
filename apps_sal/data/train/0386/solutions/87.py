class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [[1 for _ in range(5)]] + [[0 for _ in range(5)] for _ in range(n - 1)]

        for i in range(1, n):
            # a = ea + ia + ua
            dp[i][0] = dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]
            # e = ae + ie
            dp[i][1] = dp[i - 1][0] + dp[i - 1][2]
            # i = ei + oi
            dp[i][2] = dp[i - 1][1] + dp[i - 1][3]
            # o = io
            dp[i][3] = dp[i - 1][2]
            # u = iu + ou
            dp[i][4] = dp[i - 1][2] + dp[i - 1][3]

        return sum(dp[-1]) % (10 ** 9 + 7)
