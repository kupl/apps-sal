class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        
        # solution 1: Time and Space both O(N+W)
        # # pseudocode: let dp[x] be the answer when
        # #             Alice already has x points
        # dp[k] = 1.0 when K <= k <= N, else 0.0
        # for k from K-1 to 0:
        #     dp[k] = (dp[k+1] + ... + dp[k+W]) / W
        # return dp[0]
        
        # dp[x] = the answer when Alice has x points
        dp = [0.0] * (N + W + 1)
        for k in range(K, N + 1):
            # Alice wins if has between K and N points
            dp[k] = 1.0

        S = sum(dp[i] for i in range(K, K+W+1))#min(N - K + 1, W) # = dp[K+1] + ... + dp[K+W]
        # S = dp[k+1] + dp[k+2] + ... + dp[k+W]
        for k in reversed(list(range(K))):
            dp[k] = S / float(W)
            S += dp[k] - dp[k + W]

        return dp[0]
        
#         # solution 2: time and space limit exceeded
#         # dp(n, k) = 1 / W * ( sum pt in range(1, W+1) over dp(n-pt, k-pt) )
        
#         memo = {}
#         def dp(n, k):
#             if (n, k) not in memo:
#                 if k <= 0:
#                     ans = int(n >= 0)
#                 else:
#                     ans = 0
#                     for pt in range(1, W+1):
#                         ans += dp(n-pt, k-pt)
#                     ans *= 1. / W
#                 memo[n, k] = ans
#             return memo[n, k]
#         return dp(N, K)

