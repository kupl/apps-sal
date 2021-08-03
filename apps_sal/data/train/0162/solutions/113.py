class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        if(len(text1) < len(text2)):
            text1, text2 = text2, text1

        row = len(text2)
        col = len(text1) + 1

        # dp = [[0 for _ in range(col)] for _ in range(row)]

        dp = [0 for _ in range(col)]

        for i in range(row):
            pre = 0
            for j in range(1, col):

                temp = dp[j]
                if(text1[j - 1] == text2[i]):
                    dp[j] = pre + 1
                    # dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[j] = max(dp[j - 1], dp[j])
                    # dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                pre = temp

        return dp[-1]
