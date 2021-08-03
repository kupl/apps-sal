class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = dict()

        def solve(i, j):
            if i == len(text1) or j == len(text2):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                ans = 1 + solve(i + 1, j + 1)
            else:
                ans = max(solve(i + 1, j), solve(i, j + 1))

            memo[(i, j)] = ans
            return ans

        return solve(0, 0)
