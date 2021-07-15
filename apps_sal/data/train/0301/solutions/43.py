class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = [[0 for b in range(len(B)+1)] for a in range(len(A)+1)]
        
        for a in range(1, len(A)+1):
            for b in range(1, len(B)+1):
                if A[a-1] == B[b-1]:
                    dp[a][b] = dp[a-1][b-1] + 1
                else:
                    dp[a][b] = max(dp[a-1][b], dp[a][b-1])
        
        return dp[-1][-1]
