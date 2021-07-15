class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        '''
        dp[i][j][k]: the min cost to merge stone[i: j + 1] into k piles
        the range for consecutive piles of stone[i:j + 1] to be k piles after merging can be divided into two parts (for stones[:n] be finally merged into 1 pile):
            1. a sub-range from the start to the devide that is sured to be merged in to 1 pile: dp[i][divide][1]
                divide goes from start by K - 1 step to make this happen: dp[i][divide][1] < math.inf
            2. a sub-range from the divide + 1 to the end (not guaranteed to be realistic): dp[divide + 1][k - 1]
        The longer ranges are always merged from the smaller ones, no matter how the smaller ones were merged from. That is why this is a DP problem.
        '''
        n = len(stones)
        if K > 2 and n % (K - 1) != 1:
            return -1
        
        dp = [[[math.inf] * (K + 1) for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i][1] = 0
            
        presum = [stones[0]]
        for i in range(1, n):
            presum.append(presum[i - 1] + stones[i])
            
        def stones_in_range(i, j):
            return presum[j] - presum[i - 1] if i > 0 else presum[j]
        
        for rangelen in range(2, n + 1):
            for start in range(n + 1 - rangelen):
                end = start + rangelen - 1
                for k in range(2, K + 1):
                    for divide in range(start, end, K - 1):
                        dp[start][end][k] = min(dp[start][end][k], dp[start][divide][1] + dp[divide + 1][end][k - 1])
                if dp[start][end][K] < math.inf:
                    dp[start][end][1] = dp[start][end][K] + stones_in_range(start, end)
                    
        return dp[0][n - 1][1]
