class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        N = len(A)
        dp = [defaultdict(int) for _ in range(N)]
        for j in range(N):
            for i in range(j):
                t = A[j] - A[i]
                dp[j][t] = max(dp[j][t], dp[i][t] + 1)
        return max(max(col.values()) for col in dp) + 1
