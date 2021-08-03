class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        prev = [0] * (len(text2) + 1)
        curr = [0] * (len(text2) + 1)

        for row in range(len(text1)):
            for col in range(len(text2)):
                if text1[row] == text2[col]:
                    curr[col + 1] = 1 + prev[col]
                else:
                    curr[col + 1] = max(prev[col + 1], curr[col])

            prev, curr = curr, prev

        return prev[-1]
