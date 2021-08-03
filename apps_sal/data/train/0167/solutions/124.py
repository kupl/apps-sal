class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        # dp[k][m] means the number floors can be identify when using k egges with maximum try m times
        dp = [[0 for col in range(N + 2)] for row in range(K + 2)]
        m = 0
        while dp[K][m] < N:
            m += 1
            for k in range(1, K + 1):
                dp[k][m] = dp[k - 1][m - 1] + dp[k][m - 1] + 1

        return m


#         def dp(k, n):
#             if k == 1:
#                 return n
#             if n == 0:
#                 return 0
#             if (k, n) in memo:
#                 return memo[(k, n)]

#             res = sys.maxsize
#             lo, hi = 1, n
#             while lo <= hi:
#                 mid = (lo + hi) // 2
#                 broken = dp(k - 1, mid - 1)
#                 safe = dp(k, n - mid)
#                 if broken > safe:
#                     hi = mid - 1
#                     res = min(res, broken + 1)
#                 else:
#                     lo = mid + 1
#                     res = min(res, safe + 1)

#             memo[(k, n)] = res
#             return res

#         memo = {}
#         return dp(K, N)
