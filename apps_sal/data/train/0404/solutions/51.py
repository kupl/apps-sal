class Solution:

    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        dp = [[0] * (K + 1) for i in range(n)]
        total = [A[0]]
        for i in range(1, n):
            total.append(A[i] + total[i - 1])

        def solve(start, k):
            if dp[start][k] != 0:
                return dp[start][k]
            if k == 1:
                dp[start][k] = (total[n - 1] - total[start] + A[start]) / (n - start)
                return dp[start][k]
            i = start
            while i + k <= n:
                temp = (total[i] - total[start] + A[start]) / (i - start + 1) + solve(i + 1, k - 1)
                dp[start][k] = max(dp[start][k], temp)
                i += 1
            return dp[start][k]
        return solve(0, K)
