class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        #         results = [[None for _ in range(N+1)] for _ in range(K+1)]
        #         def dp(K, N):
        #             if K == 1:
        #                 return N
        #             if N == 0:
        #                 return 0

        #             if results[K][N]:
        #                 return results[K][N]

        #             res = N

        #             left = 1
        #             right = N

        #             while left <= right:
        #                 mid = int((right+left)/2)

        #                 broken_num = dp(K-1, mid-1)
        #                 notbroken_num = dp(K, N-mid)
        #                 if broken_num > notbroken_num:
        #                     right = mid - 1
        #                     res = min(res, broken_num + 1)
        #                 else:
        #                     left = mid + 1
        #                     res = min(res, notbroken_num + 1)

        #             results[K][N] = res
        #             # for i in range(1, N+1):
        #             #     results[K][N] = min(results[K][N], max(dp(K-1, i-1), dp(K, N-i)) + 1)

        #             # return results[K][N]
        #             return res
        #         # dp(K, N)
        #         # print(results)
        #         return dp(K, N)

        dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]

        m = 0
        while dp[K][m] < N:
            m += 1
            for k in range(1, K + 1):
                dp[k][m] = dp[k - 1][m - 1] + dp[k][m - 1] + 1

        return m
