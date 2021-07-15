# 1000. Minimum Cost to Merge Stones
class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        N = len(stones)
        if (N - 1) % (K - 1): 
            return -1
        dp = [[0] * N for _ in range(N)]
        
        for l in range(K, N+1):
            for i in range(N-l+1):
                dp[i][i+l-1] = float('inf')
                for x in range(i, i+l-1, K-1):
                    dp[i][i+l-1] = min(dp[i][i+l-1], dp[i][x] + dp[x+1][i+l-1])
                dp[i][i+l-1] += (sum(stones[i:i+l]) if (l-1)%(K-1) == 0 else 0)
        
        return dp[0][N-1]
