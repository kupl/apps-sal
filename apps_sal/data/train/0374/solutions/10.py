class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        def mergecost(s, t):
            c = len(t)
            for i in range(1, min(len(s), len(t))):
                if s[len(s) - i:] == t[0:i]:
                    c = len(t) - i
            return c

        n = len(A)
        cost = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                cost[i][j] = mergecost(A[i], A[j])
                cost[j][i] = mergecost(A[j], A[i])
        dp = [[float('inf') for _ in range(n)] for _ in range(1 << n)]
        parent = [[-1 for _ in range(n)] for _ in range(1 << n)]

        for i in range(n):
            dp[1 << i][i] = len(A[i])

        for s in range(1, 1 << n):
            for i in range(n):
                if not (s & (1 << i)):
                    continue
                prev = s - (1 << i)
                for j in range(n):
                    if dp[s][i] > dp[prev][j] + cost[j][i]:
                        dp[s][i] = dp[prev][j] + cost[j][i]
                        parent[s][i] = j
        minCost, end = float('inf'), 0
        for i in range(n):
            if dp[-1][i] < minCost:
                minCost = dp[-1][i]
                end = i
        s = (1 << n) - 1
        res = ''
        while s:
            prev = parent[s][end]
            if prev < 0:
                return A[end] + res
            res = A[end][len(A[end]) - cost[prev][end]:] + res
            s &= ~(1 << end)
            end = prev
        return res
