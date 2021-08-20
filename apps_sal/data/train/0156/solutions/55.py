class Solution:

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        (size1, size2) = (len(str1), len(str2))
        Inf = str1 + str2
        dp = [None] * (size2 + 1)
        dp[0] = ''
        for i in range(1, size2 + 1):
            dp[i] = dp[i - 1] + str2[i - 1]
        for i1 in range(1, size1 + 1):
            newDP = [None] * (size2 + 1)
            newDP[0] = dp[0] + str1[i1 - 1]
            for i2 in range(1, size2 + 1):
                if str1[i1 - 1] == str2[i2 - 1]:
                    newDP[i2] = dp[i2 - 1] + str1[i1 - 1]
                else:
                    newDP[i2] = min(dp[i2] + str1[i1 - 1], newDP[i2 - 1] + str2[i2 - 1], key=len)
            dp = newDP
        return dp[-1]
