class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        #         dpDict = {}

        #         def dp(K,N):
        #             if K == 1: return N
        #             if N == 0: return 0
        #             if (K, N) in dpDict: return dpDict[K,N]
        #             res = float('inf')
        #             for i in range(1, N + 1):
        #                 res = min(res,
        #                           1 + max(dp(K-1, i-1), dp(K,N-i))
        #                          )

        #             dpDict[K,N] = res
        #             return res

        #         return dp(K,N)

        dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]
        m = 0
        while dp[K][m] < N:
            m += 1
            for i in range(1, K + 1):
                dp[i][m] = dp[i][m - 1] + dp[i - 1][m - 1] + 1
        return m
