from typing import List


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # dp[i][j] 表示 text1[0:i+1] 和 text2[0:j+1] 的 Longest Common Subsequence 的长度
        # 其中 0 <= i < len(text1)
        # 其中 0 <= j < len(text2)
        dp: List[List[int]] = []
        for i in range(len(text1)):
            dp.append(len(text2) * [-1])

        def cal_with_cache(i: int, j: int):
            if i < 0 or j < 0:
                return 0

            if dp[i][j] == -1:
                dp[i][j] = cal(i, j)
            return dp[i][j]

        def cal(i: int, j: int):
            if i == 0 and j == 0:
                return 1 if text1[i] == text2[j] else 0

            if text1[i] == text2[j]:
                return cal_with_cache(i - 1, j - 1) + 1
            else:
                return max(cal_with_cache(i - 1, j), cal_with_cache(i, j - 1))

        return cal_with_cache(len(text1) - 1, len(text2) - 1)
