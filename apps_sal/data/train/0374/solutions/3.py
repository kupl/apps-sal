class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:

        def dist(s1, s2):
            ans = 0
            for k in range(min(len(s1), len(s2))):
                if s1[len(s1) - k:] == s2[:k]:
                    ans = len(s2) - k
            return ans

        n = len(A)
        g = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                g[i][j] = dist(A[i], A[j])
                g[j][i] = dist(A[j], A[i])

        parent = [[-1] * n for _ in range(1 << n)]
        dp = [[float('inf')] * n for _ in range(1 << n)]
        for i in range(n):
            dp[1 << i][i] = len(A[i])

        for s in range(1, 1 << n):
            for i in range(n):
                if not (s & (1 << i)):
                    continue
                prev = s - (1 << i)
                for j in range(n):
                    if dp[prev][j] + g[j][i] < dp[s][i]:
                        dp[s][i] = dp[prev][j] + g[j][i]
                        parent[s][i] = j

        end = dp[-1].index(min(dp[-1]))
        s = (1 << n) - 1
        res = ''
        while s:
            prev = parent[s][end]
            if prev < 0:
                res = A[end] + res
            else:
                res = A[end][len(A[end]) - g[prev][end]:] + res
            s &= ~ (1 << end)
            end = prev
        return res
