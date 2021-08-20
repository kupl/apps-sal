class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def dpRecurse(i: int, j: int):
            result = 0
            if (i, j) in memo:
                return memo[i, j]
            if i >= len(text1) or j >= len(text2):
                return 0
            elif text1[i] == text2[j]:
                result = 1 + dpRecurse(i + 1, j + 1)
            else:
                result = max(dpRecurse(i + 1, j), dpRecurse(i, j + 1))
            memo[i, j] = result
            return result
        return dpRecurse(0, 0)
