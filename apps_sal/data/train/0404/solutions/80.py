class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        if not A:
            return 0
        n = len(A)
        # Pre compute sums
        sums = [0] * (n + 1)
        # dp[k][i] stands for the answer of first i elements divided into k groups
        dp = [[float('-inf')] * (n + 1) for _ in range(K + 1)]
        for i in range(1, n + 1):
            sums[i] = sums[i - 1] + A[i - 1]
            dp[1][i] = sums[i] / i
        for k in range(2, K + 1):
            for i in range(k, n + 1):
                # Break point j from k - 1 till i
                for j in range(k - 1, i):
                    ave_i_j = (sums[i] - sums[j]) / (i - j)
                    dp[k][i] = max(dp[k][i], dp[k - 1][j] + ave_i_j)
        return dp[K][n]
