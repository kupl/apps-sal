class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = [[0] * (len(B) + 1) for _ in range(2)]
        flag = 1

        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    dp[flag][j] = dp[flag ^ 1][j + 1] + 1
                else:
                    dp[flag][j] = max(dp[flag][j + 1], dp[flag ^ 1][j])
            flag ^= 1

        return dp[flag ^ 1][0]
