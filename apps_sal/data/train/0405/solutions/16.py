class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
#         probs = [0] * (n + 1)
#         probs[0] = 1
        
#         prob = 1 / w
        
            
#         for i in range(k):
#             for j in range(1, w + 1):
#                 if i + j <= n:
#                     probs[i + j] += probs[i] * prob
        
#         return sum(probs[k : n + 1])
        
        dp = [0.0] * (N + W + 1)
        # dp[x] = the answer when Alice has x points
        for k in range(K, N + 1):
            dp[k] = 1.0

        S = min(N - K + 1, W)
        # S = dp[k+1] + dp[k+2] + ... + dp[k+W]
        for k in range(K - 1, -1, -1):
            dp[k] = S / float(W)
            S += dp[k] - dp[k + W]

        return dp[0]
