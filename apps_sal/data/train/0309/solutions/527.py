class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        sol = 1
        dp = {}
        for j in range(1,n):
            for i in range(j):
                diff = A[j] - A[i]
                dp[j,diff] = max(dp.get((j,diff), 2), dp.get((i,diff),1)+1)
                sol = max(sol, dp[j,diff])
                
        return sol
