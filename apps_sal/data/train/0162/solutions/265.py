class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0:
            return ''
        DP = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
        longest = 0
        for i in range(1, len(text2) + 1):
            for j in range(1, len(text1) + 1):
                if text2[i - 1] == text1[j - 1]:
                    DP[i][j] = max(max(DP[i - 1][j - 1] + 1, DP[i - 1][j]), DP[i][j - 1])
                else:
                    DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])
                longest = max(longest, DP[i][j])
        return longest
