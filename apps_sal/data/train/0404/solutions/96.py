class Solution:

    def largestSumOfAverages(self, A, K):
        dp = {}

        def search(n, k):
            if (n, k) in dp:
                return dp[n, k]
            if n < k:
                return 0
            if k == 1:
                dp[n, k] = sum(A[:n]) / float(n)
                return dp[n, k]
            (cur, dp[n, k]) = (0, 0)
            for i in range(n - 1, 0, -1):
                cur += A[i]
                dp[n, k] = max(dp[n, k], search(i, k - 1) + cur / float(n - i))
            return dp[n, k]
        return search(len(A), K)
