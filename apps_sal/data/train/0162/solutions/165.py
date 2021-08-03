class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}

        def inner(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0

            if dp.get((i, j)) == None:
                if text1[i] == text2[j]:
                    dp[(i, j)] = inner(i + 1, j + 1) + 1
                else:
                    dp[(i, j)] = max(inner(i + 1, j), inner(i, j + 1))
            return dp[(i, j)]
        return inner(0, 0)
