class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) < len(text1):
            (text1, text2) = (text2, text1)
        prev = [0] * (len(text1) + 1)
        for row in range(1, len(text2) + 1):
            curr = [0] * (len(text1) + 1)
            for col in range(1, len(text1) + 1):
                if text2[row - 1] == text1[col - 1]:
                    curr[col] = prev[col - 1] + 1
                else:
                    curr[col] = max(prev[col], curr[col - 1])
            prev = curr
        return prev[-1]
