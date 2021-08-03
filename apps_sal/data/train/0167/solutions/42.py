class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [i for i in range(N + 1)]
        for j in range(1, K):
            prev = dp.copy()
            m = 1
            for i in range(2, N + 1):
                while m < i and dp[i - m] >= prev[m - 1] and dp[i - m - 1] >= prev[m]:
                    m += 1
                dp[i] = max(dp[i - m], prev[m - 1]) + 1
        return dp[N]
