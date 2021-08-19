class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0 for i in range(N + 1)] for j in range(K + 1)]
        m = 0
        while dp[K][m] < N:
            m += 1
            for k in range(1, K + 1):
                dp[k][m] = dp[k - 1][m - 1] + dp[k][m - 1] + 1
        return m
