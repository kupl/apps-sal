class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        sum_i2end = [0] * (n + 1)
        for i in range(1, n + 1):
            sum_i2end[i] = sum_i2end[i - 1] + A[i - 1]

        dp = [0] * n
        for i in range(n):
            dp[i] = (sum_i2end[-1] - sum_i2end[i]) / (n - i)

        for _ in range(K - 1):
            for i in range(n):
                for j in range(i + 1, n):
                    dp[i] = max(dp[i], dp[j] + ((sum_i2end[j] - sum_i2end[i]) / (j - i)))
        return dp[0]
