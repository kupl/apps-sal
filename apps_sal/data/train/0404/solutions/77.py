class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        prefix_sum = [A[0]]
        for a in A[1:]:
            prefix_sum.append(prefix_sum[-1] + a)
        dp = [[0 for _ in range(len(A))] for _ in range(K)]
        for i in range(len(A)):
            dp[0][i] = prefix_sum[i] / (i + 1)
        for k in range(1, K):
            for i in range(k, len(A)):
                for j in range(k - 1, i):
                    dp[k][i] = max(dp[k][i], dp[k - 1][j] + (prefix_sum[i] - prefix_sum[j]) / (i - j))
        return dp[K - 1][len(A) - 1]
