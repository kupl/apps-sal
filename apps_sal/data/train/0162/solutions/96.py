class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        hist = {}

        def helper(str1, str2, m, n):
            if (m, n) in hist:
                return hist[m, n]
            if m == 0 or n == 0:
                return 0
            elif str1[m - 1] == str2[n - 1]:
                hist[m, n] = 1 + helper(str1, str2, m - 1, n - 1)
                return hist[m, n]
            hist[m, n] = max(helper(str1, str2, m - 1, n), helper(str1, str2, m, n - 1))
            return hist[m, n]
        return helper(text1, text2, len(text1), len(text2))
