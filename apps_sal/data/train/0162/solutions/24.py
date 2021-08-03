class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:
        n1, n2 = len(a), len(b)
        memo = [[None] * (n2 + 1) for i in range(n1 + 1)]

        def helper(i, j):
            if memo[i][j] == None:
                if i == n1 or j == n2:
                    memo[i][j] = 0

                elif a[i] == b[j]:
                    return 1 + helper(i + 1, j + 1)
                else:
                    memo[i][j] = max(helper(i, j + 1), helper(i + 1, j))
            return memo[i][j]

        return helper(0, 0)
