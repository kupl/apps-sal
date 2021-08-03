class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0

        cacheRow = [None] * len(text2)
        cache = [cacheRow[:] for i in range(len(text1))]
        return self.dp(text1, text2, 0, 0, cache)

    def dp(self, text1, text2, i, j, cache):
        if i >= len(text1) or j >= len(text2):
            return 0

        if cache[i][j] is None:
            if text1[i] == text2[j]:
                cache[i][j] = 1 + self.dp(text1, text2, i + 1, j + 1, cache)
            else:
                cache[i][j] = max(self.dp(text1, text2, i + 1, j, cache), self.dp(text1, text2, i, j + 1, cache))

        return cache[i][j]
