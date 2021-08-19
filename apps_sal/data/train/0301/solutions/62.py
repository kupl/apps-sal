class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        max_lines = 0
        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                temp = int(A[i - 1] == B[j - 1])
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + temp)
        return dp[-1][-1]
