class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        maxes = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n):
            maxes[i][i] = arr[i]
        for i in range(n):
            for j in range(i + 1, n):
                maxes[i][j] = max(arr[j], maxes[i][j - 1])

        dp = [None for _ in range(n + 1)]
        dp[n] = 0
        for i in range(n - 1, -1, -1):
            m = float('-inf')
            for j in range(min(n - i, k)):
                m = max(m, (j + 1) * maxes[i][min(n - 1, i + j)] + dp[min(n, i + j + 1)])
            dp[i] = m
        return dp[0]
