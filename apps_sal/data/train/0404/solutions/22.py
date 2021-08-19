class Solution:

    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        N = len(A)
        summary = [0] * (N + 1)
        for (i, item) in enumerate(A):
            summary[i + 1] = summary[i] + item
        dp = [[(summary[N] - summary[i]) / (N - i) for i in range(N)] for _ in range(K)]
        for remain in range(1, K):
            for i in range(N):
                for j in range(i + 1, N):
                    dp[remain][i] = max(dp[remain][i], (summary[j] - summary[i]) / (j - i) + dp[remain - 1][j])
        return dp[-1][0]
