class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        memorize = [[-1] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        def LCS(i1, i2):
            if i1 >= len(text1) or i2 >= len(text2):
                return 0
            if memorize[i1][i2] != -1:
                return memorize[i1][i2]

            if text1[i1] == text2[i2]:
                memorize[i1][i2] = 1 + LCS(i1 + 1, i2 + 1)
            else:
                memorize[i1][i2] = max(LCS(i1, i2 + 1), LCS(i1 + 1, i2))
            return memorize[i1][i2]

        ans = LCS(0, 0)
        return ans
