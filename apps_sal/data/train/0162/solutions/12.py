from functools import lru_cache


class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 = len(text1)
        l2 = len(text2)
        memo = [[0 for _ in range(max(l1, l2) + 1)] for _ in range(max(l1, l2) + 1)]
        current = 0
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                current = memo[i - 1][j - 1]
                if text1[i - 1] == text2[j - 1]:
                    memo[i][j] = 1 + memo[i - 1][j - 1]
                else:
                    memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])
                current = max(memo[i][j], current)
        return current
