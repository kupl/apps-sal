class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        N = len(A)
        ans = 2
        dp = [{} for _ in range(N)]
        for i in range(N):
            for j in range(i):
                diff = A[j] - A[i]
                dp[i][diff] = dp[j].get(diff,1)+1
                ans = max(ans,dp[i][diff])
        return ans
