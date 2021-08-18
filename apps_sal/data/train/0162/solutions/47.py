class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @lru_cache(None)
        def longest(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            elif text1[i] == text2[j]:
                return 1 + longest(i + 1, j + 1)
            else:
                return max(longest(i, j + 1), longest(i + 1, j))

        return longest(0, 0)
