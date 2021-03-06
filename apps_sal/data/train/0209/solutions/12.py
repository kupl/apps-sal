class Solution:

    def mergeStones(self, stones: List[int], K: int) -> int:
        n = len(stones)
        dp = [[[math.inf for k in range(K + 1)] for j in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i][1] = 0
        pre_sum = [0] * n
        pre_sum[0] = stones[0]
        for i in range(1, n):
            pre_sum[i] = pre_sum[i - 1] + stones[i]

        def range_sum(i, j):
            if i == 0:
                return pre_sum[j]
            else:
                return pre_sum[j] - pre_sum[i - 1]
        for merge_len in range(2, n + 1):
            for start in range(n - merge_len + 1):
                end = start + merge_len - 1
                for k in range(2, K + 1):
                    for middle in range(start, end, K - 1):
                        dp[start][end][k] = min(dp[start][end][k], dp[start][middle][1] + dp[middle + 1][end][k - 1])
                if dp[start][end][K] < math.inf:
                    dp[start][end][1] = dp[start][end][K] + range_sum(start, end)
        return dp[0][n - 1][1] if dp[0][n - 1][1] < math.inf else -1
