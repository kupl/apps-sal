class Solution:

    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        if s1 == '' or s2 == '':
            return 0
        dp = [[0 for y in s2] for x in s1]
        for i in range(0, len(s1)):
            for j in range(0, len(s2)):
                if i == 0 and j == 0:
                    dp[i][j] = 1 if s1[i] == s2[j] else 0
                elif i == 0:
                    dp[i][j] = 1 if s1[i] == s2[j] else dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = 1 if s1[i] == s2[j] else dp[i - 1][j]
                else:
                    dp[i][j] = max([dp[i - 1][j - 1] + 1 if s1[i] == s2[j] else 0, dp[i - 1][j], dp[i][j - 1]])
        return dp[-1][-1]
