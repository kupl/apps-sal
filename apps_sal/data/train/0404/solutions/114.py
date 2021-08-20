class Solution:

    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        prefixSum = [0]
        for x in A:
            prefixSum.append(prefixSum[-1] + x)

        def avg(i, j):
            return (prefixSum[j] - prefixSum[i]) / (j - i)
        n = len(A)
        dp = [avg(i, n) for i in range(n)]
        for k in range(K - 1):
            for i in range(n):
                for j in range(i + 1, n):
                    dp[i] = max(dp[i], avg(i, j) + dp[j])
        return dp[0]
