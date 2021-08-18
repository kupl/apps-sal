

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def lcs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == len(text1) or j == len(text2):
                return 0

            move_both = None
            if text1[i] == text2[j]:
                move_both = 1 + lcs(i + 1, j + 1)

            move_i = lcs(i + 1, j)
            move_j = lcs(i, j + 1)
            memo[(i, j)] = max(move_i, move_j) if move_both is None else max([move_i, move_j, move_both])
            return memo[(i, j)]

        return lcs(0, 0)
