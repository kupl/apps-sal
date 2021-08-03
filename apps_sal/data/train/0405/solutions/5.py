class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0:
            return 1
        dp = [0] * (W + K)
        dp[0] = 1
        sliding_sum = 1
        for i in range(1, K + W):
            # print(sliding_sum)
            # constant = dp[i] / W
            # for j in range(i+1, i+W+1):
            #     dp[j] += constant
            # dp[i] = 0
            dp[i] = sliding_sum / W
            if i < K:
                sliding_sum += dp[i]
            if i - W >= 0:
                sliding_sum -= dp[i - W]
                dp[i - W] = 0
        # print(dp)
        return sum(dp[K:N + 1]) / sum(dp)
