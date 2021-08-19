import numpy as np


class Solution:

    def shortestSuperstring(self, A: List[str]) -> str:
        n = len(A)
        g = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                g[i][j] = len(A[j])
                k = 1
                while k <= min(len(A[i]), len(A[j])):
                    if A[i][len(A[i]) - k:] == A[j][:k]:
                        g[i][j] = len(A[j]) - k
                    k += 1
        dp = [[float('inf')] * n for _ in range(1 << n)]
        parent = [[-1] * n for _ in range(1 << n)]
        for i in range(n):
            dp[1 << i][i] = len(A[i])
        for s in range(1, 1 << n):
            for j in range(n):
                if not s & 1 << j:
                    continue
                ps = s & ~(1 << j)
                for i in range(n):
                    if dp[ps][i] + g[i][j] < dp[s][j]:
                        dp[s][j] = dp[ps][i] + g[i][j]
                        parent[s][j] = i
        j = np.argmin(dp[-1])
        s = (1 << n) - 1
        ans = ''
        while s:
            i = parent[s][j]
            if i < 0:
                ans = A[j] + ans
            else:
                ans = A[j][len(A[j]) - g[i][j]:] + ans
            s &= ~(1 << j)
            j = i
        return ans
