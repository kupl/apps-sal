from collections import defaultdict


class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = defaultdict(lambda: -1)

        def helper(text1, n, text2, m):
            if m == 0 or n == 0:
                return 0
            if dp[m, n] == -1:
                if text1[-1] == text2[-1]:
                    length = 1 + helper(text1[:-1], n - 1, text2[:-1], m - 1)
                else:
                    length = max(helper(text1[:-1], n - 1, text2, m), helper(text1, n, text2[:-1], m - 1))
                dp[m, n] = length
            return dp[m, n]
        return helper(text1, len(text1), text2, len(text2))
