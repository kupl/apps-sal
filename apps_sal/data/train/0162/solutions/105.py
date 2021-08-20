class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def helper(text1, text2, i, j, memo):
            if i == len(text1) or j == len(text2):
                return 0
            if memo[i][j] < 0:
                c1 = text1[i]
                c2 = text2[j]
                if c1 == c2:
                    memo[i + 1][j + 1] = helper(text1, text2, i + 1, j + 1, memo)
                    memo[i][j] = 1 + memo[i + 1][j + 1]
                else:
                    memo[i + 1][j] = helper(text1, text2, i + 1, j, memo)
                    memo[i][j + 1] = helper(text1, text2, i, j + 1, memo)
                    memo[i][j] = max(memo[i + 1][j], memo[i][j + 1])
            return memo[i][j]
        n = len(text1)
        m = len(text2)
        memo = [[-1 for _ in range(0, m + 1)] for _ in range(0, n + 1)]
        return helper(text1, text2, 0, 0, memo)
