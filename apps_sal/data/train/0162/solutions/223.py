class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # use dynamic programming

        # initialize table to store sub solutions
        # row (i) = index of text1 + 0 for initial row
        # column (j) = index of text2 + 0 for initial row
        # cell = max length of subsequence for text1[1:i] text2[1:j]
        t = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

        # loop through each element
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                # if text is the same, diagonal cell + 1
                if text1[i - 1] == text2[j - 1]:
                    t[i][j] = t[i - 1][j - 1] + 1
                # else, max of above (not considering last of text 1) or left
                else:
                    t[i][j] = max(t[i - 1][j], t[i][j - 1])

        # return right bottom of table
        return t[len(text1)][len(text2)]
