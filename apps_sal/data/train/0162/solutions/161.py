class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        set1, set2 = set(text1), set(text2)
        if not set1.intersection(set2):
            return 0

        dp = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                tmp = 0
                if text1[i - 1] == text2[j - 1]:
                    tmp = 1
                dp[i][j] = max([dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + tmp])

        return dp[-1][-1]
