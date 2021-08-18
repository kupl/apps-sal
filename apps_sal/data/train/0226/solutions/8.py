import math


class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        n = len(A)
        A = sorted(A)
        g = [[False] * n for _ in range(n)]
        dp = [[0] * n for _ in range(1 << n)]

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if int((A[i] + A[j]) ** 0.5 + 0.5) ** 2 == A[i] + A[j]:
                    g[i][j] = True

        for i in range(n):
            if i > 0 and A[i] == A[i - 1]:
                continue
            dp[1 << i][i] = 1

        for s in range(1 << n):
            for i in range(n):
                if dp[s][i] <= 0:
                    continue
                for j in range(n):
                    if not g[i][j] or (s & (1 << j)):
                        continue
                    if j > 0 and not (s & (1 << (j - 1))) and A[j] == A[j - 1]:
                        continue
                    dp[s | (1 << j)][j] += dp[s][i]

        res = 0
        for i in range(n):
            res += dp[(1 << n) - 1][i]
        return res
