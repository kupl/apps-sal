class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        s1, s2 = len(text1), len(text2)
        # init
        res = 0
        dp = [[0 for _ in range(s2 + 1)] for _ in range(s1 + 1)]
        # dp[i][j] = dp[i-1][j-1] + 1 if text1[i]==text2[j]
        #            dp[i-1][j-1]      else

        for i in range(1, s1 + 1):
            for j in range(1, s2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                res = max(dp[i][j], res)
        return res
        # boundary: 0 <= max_common <= min(len(tex1), len(text2))
