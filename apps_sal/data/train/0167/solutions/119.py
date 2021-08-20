class Solution:

    def superEggDrop(self, K, N):
        dp = [0, 0]
        m = 0
        while dp[-1] < N:
            for i in range(len(dp) - 1, 0, -1):
                dp[i] += dp[i - 1] + 1
            if len(dp) < K + 1:
                dp.append(dp[-1])
            m += 1
        return m
