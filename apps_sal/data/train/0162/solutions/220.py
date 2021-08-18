class Solution:
    def helper(self, text1, text2, index1, index2, match):
        if index1 == len(text1) or index2 == len(text2):
            return match
        s1 = 0
        s2 = 0
        s3 = 0
        if text1[index1] == text2[index2]:
            s1 = self.helper(text1, text2, index1 + 1, index2 + 1, match + 1)
        else:
            s2 = self.helper(text1, text2, index1, index2 + 1, match)
            s3 = self.helper(text1, text2, index1 + 1, index2, match)

        return max(s1, s2, s3)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        if not text1 or not text2:
            return 0

        dp = [[0 for i in range(len(text1) + 1)] for j in range(len(text2) + 1)]

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):

                if text1[j - 1] == text2[i - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[len(text2)][len(text1)]
