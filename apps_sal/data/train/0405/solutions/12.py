class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if N > K + W - 1 or K == 0: return 1
        
        dp = [0] * (K + W)
        dp[1] = 1 / W
        for i in range(2, K + 1):
            if i == W + 1:
                dp[i] = dp[i - 1] + (dp[W] - 1) / W
            else:
                dp[i] = ((W + 1) * dp[i - 1] - (dp[i - 1 - W] if i >= W + 1 else 0)) / W
        for i in range(K + 1, K + W):
            dp[i] = dp[i - 1] - (dp[i - W - 1] if i - W >= 2 else 0) / W
            if i == W + 1: dp[i] -= 1 / W
        res = sum(dp[i] for i in range(K, N + 1)) / sum(dp[i] for i in range(K, K + W))
        return res
