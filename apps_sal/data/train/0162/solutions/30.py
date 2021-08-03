class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @lru_cache(None)
        def recur(i, j):
            if i == -1 or j == -1:
                return 0

            if text1[i] == text2[j]:
                return recur(i - 1, j - 1) + 1
            else:
                return max(recur(i - 1, j), recur(i, j - 1))

        return recur(len(text1) - 1, len(text2) - 1)
