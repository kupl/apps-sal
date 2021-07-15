class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        N = len(stones)
        presum = [0 for _ in range(N + 1)]
        dp = [[[math.inf for _ in range(K + 1)] for _ in range(N)] for _ in range(N)]
        
        if (N - 1) % (K - 1) != 0:
            return -1
        
        for i in range(N):
            presum[i + 1] = presum[i] + stones[i]
            
        for i in range(N):
            dp[i][i][1] = 0
        
        for length in range(2, N + 1):
            for start in range(N - length + 1):
                end = start + length - 1
                for mid in range(start, end):
                    for k in range(2, K + 1):
                        if k > length: 
                            continue
                        if dp[start][mid][1] == math.inf or dp[mid + 1][end][k - 1] == math.inf:
                            continue
                            
                        dp[start][end][k] = min(dp[start][end][k], dp[start][mid][1] + dp[mid + 1][end][k - 1])
                    
                    if dp[start][end][K] != math.inf:
                        dp[start][end][1] = dp[start][end][K] + presum[end + 1] - presum[start]
                    
        if dp[0][N - 1][1] == math.inf:
            return -1
        return dp[0][N - 1][1]
