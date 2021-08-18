class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def s(i, j, cache):
            if i < 0 or j < 0:
                return 0
            p = (i, j)
            if p not in cache:
                if text1[i] == text2[j]:
                    cache[p] = 1 + s(i - 1, j - 1, cache)
                else:
                    cache[p] = max(s(i, j - 1, cache), s(i - 1, j, cache))
            return cache[p]
        cache = {}
        return s(len(text1) - 1, len(text2) - 1, cache)
