import numpy as np


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)
        if l1 == l2 and text1 == text2:
            return l1
        if l1 < l2:
            text1, text2, l1, l2 = text2, text1, l2, l1
        mat_ = np.zeros((l2 + 1, l1 + 1))
        for j in range(1, l2 + 1):
            for i in range(1, l1 + 1):
                if text2[j - 1] == text1[i - 1]:
                    mat_[j, i] = 1 + mat_[j - 1, i - 1]
                else:
                    mat_[j, i] = max(mat_[j, max(0, i - 1)], mat_[max(0, j - 1), i])
        return int(mat_[-1][-1])
