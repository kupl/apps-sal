class Solution:

    def minScoreTriangulation(self, A: List[int]) -> int:
        N = len(A)
        if N == 3:
            return A[0] * A[1] * A[2]

        def solver(s, t, A):
            if t - s + 1 < 3:
                return 0
            if dp[s][t] != float('inf'):
                return dp[s][t]
            for i in range(s + 1, t):
                dp[s][t] = min(dp[s][t], solver(s, i, A) + A[s] * A[i] * A[t] + solver(i, t, A))
            return dp[s][t]
        dp = []
        for i in range(N):
            dp.append([float('inf')] * N)
        return solver(0, N - 1, A)
