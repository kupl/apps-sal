class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = [[0 for _ in B] for _ in A]
        for i in range(len(B)):
            if A[0] == B[i]:
                dp[0][i] = 1
            elif i != 0:
                dp[0][i] = dp[0][i-1]
        for i in range(len(A)):
            if B[0] == A[i]:
                dp[i][0] = 1
            elif i != 0:
                dp[i][0] = dp[i-1][0]
        for i in range(1,len(A)):
            for j in range(1,len(B)):
                if A[i] == B[j]:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+1)
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        return dp[-1][-1]

