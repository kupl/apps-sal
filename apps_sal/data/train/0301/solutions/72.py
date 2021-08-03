class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:

        a, b = len(A), len(B)
        dp = {}
        for i, num1 in enumerate(A):
            for j, num2 in enumerate(B):
                if num1 == num2:
                    dp[(i, j)] = 1 + dp[i - 1, j - 1] if min(i, j) > 0 else 1
                else:
                    dp[(i, j)] = max(dp[i - 1, j] if i > 0 else 0,
                                     dp[i, j - 1] if j > 0 else 0
                                     )

        return dp[a - 1, b - 1]
