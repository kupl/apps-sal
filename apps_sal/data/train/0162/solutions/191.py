class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = []
        for i in range(m + 1):
            dp.append([0] * (n + 1))
        for i in range(1, m + 1):
            text1_sub = text1[:i]
            for j in range(1, n + 1):
                ch = text2[j - 1]
                options = [dp[i][j - 1]]
                last_idx = i - text1_sub[::-1].find(ch) - 1
                if last_idx != i:
                    options.append(1 + dp[last_idx][j - 1])
                dp[i][j] = max(options)
        return dp[m][n]
