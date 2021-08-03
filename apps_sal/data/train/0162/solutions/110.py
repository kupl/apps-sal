class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}

        def dfs(i, j, count):

            if i == len(text1) or j == len(text2):
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            if text1[i] == text2[j]:
                #count += 1
                return 1 + dfs(i + 1, j + 1, count)

            a = dfs(i + 1, j, count)
            b = dfs(i, j + 1, count)
            c = max(a, b)

            cache[(i, j)] = c
            return c

        return dfs(0, 0, 0)
