class Solution:
    def superEggDrop(self, K: int, N: int) -> int:

        # dp = [[0 for _ in range(N+1)] for _ in range(K+1)]

        dp = list(range(N + 1))
        for i in range(2, K + 1):
            k = 1
            temp = [0] + [N + 1] * (N)
            for j in range(1, N + 1):
                while k < j + 1 and temp[j - k] > dp[k - 1]:
                    k += 1
                temp[j] = 1 + dp[k - 1]
                # if i > j:
                #     dp[i][j] = dp[i-1][j]
                # else:
                #     val = N + 1
                #     for k in range(1, j+1):
                #         val = min(val, 1 + max(dp[i-1][k-1], dp[i][j-k]))
                #     dp[i][j] = val
            dp = temp[:]
        # print(dp)
        return dp[-1]
