class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0] * (N + 1) for _ in range(K + 1)]
        for k in range(1, K + 1):
            for n in range(1, N + 1):
                if k == 1:
                    dp[k][n] = n
                else:
                    dp[k][n] = 1 + dp[k - 1][n - 1] + dp[k][n - 1]
        (top, bott) = (0, N)
        while top < bott:
            mid = (top + bott) // 2
            if dp[K][mid] < N:
                top = mid + 1
            else:
                bott = mid
        return bott
