class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[float('inf')] * (N+1) for _ in range(K+1)]
        for k in range(1, K+1):
            dp[k][1] = 1
            dp[k][0] = 0
        for n in range(1, N+1):
            dp[1][n] = n
        
        for k in range(2, K+1):
            x = 1
            for n in range(2, N+1):
                while x < n+1 and dp[k][n-x] > dp[k-1][x-1]:
                    x += 1
                dp[k][n] = 1 + dp[k-1][x-1]
        #print(dp)
        return dp[-1][-1]
