class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:

        memo = {}

        def dfs(n, K):

            if (n, K) in memo:
                return memo[n, K]

            if n < K:
                return 0

            if K == 1:
                memo[n, K] = sum(A[:n]) / n
                return memo[n, K]

            cur, memo[n, K] = 0, 0
            for i in range(n - 1, 0, -1):
                cur += A[i]
                memo[n, K] = max(memo[n, K], dfs(i, K - 1) + cur / (n - i))

            return memo[n, K]

        return dfs(len(A), K)
