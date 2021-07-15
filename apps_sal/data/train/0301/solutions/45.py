class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        lenA, lenB = len(A), len(B)
        dp = [[0 for _ in range(lenB+1)] for _ in range(lenA + 1) ]
        for i in range(lenA):
            for j in range(lenB):
                if A[i]==B[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        #print(dp)
        return dp[lenA][lenB]

