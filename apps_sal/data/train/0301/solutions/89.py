class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = defaultdict(int)
        (N, M) = (len(A), len(B))
        for i in range(N):
            for j in range(M):
                dp[i, j] = max(dp[i - 1, j - 1] + (A[i] == B[j]), dp[i - 1, j], dp[i, j - 1])
        return dp[N - 1, M - 1]
