class Solution:

    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        if K >= n:
            return sum(A)
        pre_sum = [0]
        for num in A:
            pre_sum.append(pre_sum[-1] + num)
        if K <= 1:
            return pre_sum[-1] / n
        dp = [[0] * (K + 1) for _ in range(n)]
        dp[0][1] = A[0]
        for i in range(1, n):
            dp[i][1] = pre_sum[i + 1] / (1 + i)
        for k in range(2, K + 1):
            for i in range(k - 1, n):
                for j in range(k - 2, i):
                    dp[i][k] = max(dp[i][k], dp[j][k - 1] + (pre_sum[i + 1] - pre_sum[j + 1]) / (i - j))
        print(dp)
        return dp[n - 1][K]
