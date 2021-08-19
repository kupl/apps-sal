class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for i in range(len(text2))] for j in range(len(text1))]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = (dp[i - 1][j - 1] if i > 0 and j > 0 else 0) + 1
                else:
                    p1 = dp[i - 1][j] if i > 0 else 0
                    p2 = dp[i][j - 1] if j > 0 else 0
                    p3 = dp[i - 1][j - 1] if i > 0 and j > 0 else 0
                    max_num = max(p1, p2, p3)
                    dp[i][j] = max_num
        return dp[-1][-1]
