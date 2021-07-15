class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        N = len(A)
        dp = [[2] * N for i in range(N)]
        ans = 0
        for i in range(N):
            pos = {}
            for j in range(i):
                x = 2*A[j] - A[i]
                if x in pos:
                    dp[i][j] = max(dp[i][j], 1 + dp[j][pos[x]])
                ans = max(ans, dp[i][j])
                pos[A[j]] = j
        
        return ans
