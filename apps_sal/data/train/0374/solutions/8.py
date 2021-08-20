class Solution:

    def shortestSuperstring(self, A: List[str]) -> str:
        n = len(A)
        g = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                g[i][j] = len(A[j])
                s = 0
                for s in range(min(len(A[i]), len(A[j]))):
                    if A[i][len(A[i]) - s:] == A[j][:s]:
                        g[i][j] = len(A[j]) - s
        dp = [[float('inf')] * n for _ in range(2 ** n)]
        parent = [[-1] * n for _ in range(2 ** n)]
        for i in range(n):
            dp[2 ** i][i] = len(A[i])
        for s in range(1, 2 ** n):
            for i in range(n):
                if s & 2 ** i == 0:
                    continue
                pre = s & ~(1 << i)
                for j in range(n):
                    if dp[pre][j] + g[j][i] < dp[s][i]:
                        dp[s][i] = dp[pre][j] + g[j][i]
                        parent[s][i] = j
        j = dp[-1].index(min(dp[-1]))
        s = 2 ** n - 1
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
