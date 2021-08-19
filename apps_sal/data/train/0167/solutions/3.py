class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0] * (N + 1) for _ in range(K + 1)]
        # dp[k][n]: the max floor number we can cover with k eggs and n drops
        # if k = 1, dp[1][n] = n
        # if k >= 2, after one drop, n-1 drops left, two cases:
        #            if the egg breaks, k-1 egges, thus dp[k-1][n-1]
        #            if it doesn't break, k egges, thus dp[k][n-1]
        # just leave the 0 col and 0 row blank
        # when k = 1
        # when k >= 2
        for k in range(1, K + 1):
            for n in range(1, N + 1):
                if k == 1:
                    dp[k][n] = n
                else:
                    dp[k][n] = 1 + dp[k - 1][n - 1] + dp[k][n - 1]
        # find the smallest n in the last row with dp[K,n] > N
        top, bott = 0, N
        while top < bott:
            mid = (top + bott) // 2
            if dp[K][mid] < N:
                top = mid + 1
            else:
                bott = mid
        return bott
