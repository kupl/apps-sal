class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:

        N = len(A)
        dp = [{} for _ in range(N)]
        for i in range(1, N):
            for j in range(0, i):
                dp[i][A[i] - A[j]] = dp[j].get(A[i] - A[j], 0) + 1
        max_len = 0
        for i in range(1, N):
            max_len = max(max_len, max(dp[i].values()))
        return max_len + 1
