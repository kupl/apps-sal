class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
        
        attempt = 0 
        while dp[attempt][K] < N:
            attempt += 1 
            for i in range(1, K+1):
                dp[attempt][i] = 1 + dp[attempt-1][i-1] + dp[attempt-1][i]
                if dp[attempt][i] >= N :
                    return attempt
        
        return attempt
