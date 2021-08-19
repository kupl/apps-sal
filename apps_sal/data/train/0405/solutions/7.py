class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0 or K - 1 + W <= N:
            return 1
        dp = [1] + [0] * N
        cursum = 1
        for i in range(1, N + 1):
            # dp[i]=sum(dp[max(0,i-W):min(i,K)])*(1/W)
            dp[i] = cursum * (1 / W)
            if i < K:
                cursum += dp[i]
            if i >= W:
                cursum -= dp[i - W]
        return sum(dp[K:])
