class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # dp[i][j]: for 0-ith elements, the length of subsquence when step = j
        # dp[i][j] = dp[i-1][A[i]-A[k]] + 1 where k = 0, 1, ...i-1
        # return max(dp[n-1][j])
        # base case dp[0][0] = 1
        
        N = len(A)
        dp = [{} for _ in range(N)]
        for i in range(1, N):
            for j in range(0, i):
                dp[i][A[i]-A[j]] = dp[j].get(A[i]-A[j], 0) + 1
        max_len = 0
        for i in range(1, N):
            max_len = max(max_len, max(dp[i].values()))
        return max_len + 1
