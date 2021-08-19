import math


class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        if m == 0 or n == 0:
            return 0
        mat = [[-math.inf] * (n + 1) for _ in range(m + 1)]
        prev = [0] * (n + 1)
        curr = [0] + [-math.inf] * n
        for a in range(1, m + 1):
            for b in range(1, n + 1):
                if text1[a - 1] == text2[b - 1]:
                    curr[b] = 1 + prev[b - 1]
                else:
                    curr[b] = max(curr[b - 1], prev[b])
            prev = curr
            curr = [0] + [-math.inf] * n
        return prev[n]
