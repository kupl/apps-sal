from typing import List


class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
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
