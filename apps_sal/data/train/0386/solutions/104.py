class Solution:

    def countVowelPermutation(self, n: int) -> int:
        dp = [[0, 0, 0, 0, 0] for i in range(n)]
        dp[0] = [1, 1, 1, 1, 1]
        for m in range(1, n):
            dp[m][0] = dp[m - 1][1] + dp[m - 1][2] + dp[m - 1][4]
            dp[m][1] = dp[m - 1][0] + dp[m - 1][2]
            dp[m][2] = dp[m - 1][1] + dp[m - 1][3]
            dp[m][3] = dp[m - 1][2]
            dp[m][4] = dp[m - 1][2] + dp[m - 1][3]
        return sum(dp[-1]) % (pow(10, 9) + 7)
