class Solution:

    def shortestSuperstring(self, A: List[str]) -> str:
        n = len(A)
        overlaps = [[0] * n for _ in range(n)]
        for (i, x) in enumerate(A):
            for (j, y) in enumerate(A):
                for ans in range(min(len(x), len(y)), -1, -1):
                    if x.endswith(y[:ans]):
                        overlaps[i][j] = ans
                        break
        maxv = 20 * n + 1
        dp = [[maxv] * n for _ in range(1 << n)]
        parent = [[-1] * n for _ in range(1 << n)]
        for i in range(n):
            dp[1 << i][i] = len(A[i])
        for s in range(1, 1 << n):
            for i in range(n):
                if not s & 1 << i:
                    continue
                prev = s - (1 << i)
                for j in range(n):
                    if dp[prev][j] + len(A[i]) - overlaps[j][i] < dp[s][i]:
                        dp[s][i] = dp[prev][j] + len(A[i]) - overlaps[j][i]
                        parent[s][i] = j
        path = []
        (s, i) = ((1 << n) - 1, 0)
        for j in range(1, n):
            if dp[s][j] < dp[s][i]:
                i = j
        path.append(i)
        while len(path) < n:
            j = parent[s][i]
            path.append(j)
            prev = s ^ 1 << i
            (s, i) = (prev, j)
        i = path[-1]
        res = [A[i]]
        for j in path[::-1][1:]:
            res.append(A[j][overlaps[i][j]:])
            i = j
        return ''.join(res)
