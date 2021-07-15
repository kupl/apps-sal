class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        # dp[i][j][k]: min cost of merging from i to j and finally having k piles
        n = len(stones)
        dp = [[[math.inf for k in range(K + 1)] for _ in range(n)] for _ in range(n)]
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
        
        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                # 最少两个，最多K个pile
                for k in range(2, K + 1):
                    for middle in range(i, j, K-1):
                        # 分成 1 和 k-1堆，合并起来是 k
                        dp[i][j][k] = min(dp[i][j][k], dp[i][middle][1] + dp[middle + 1][j][k - 1])
                if dp[i][j][K] < math.inf:
                    # 合并成 1个pile
                    dp[i][j][1] = dp[i][j][K] + range_sum(i, j)
        return dp[0][n-1][1] if dp[0][n - 1][1] < math.inf else -1

