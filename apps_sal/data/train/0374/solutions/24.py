class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        ''' TSP: DP '''
        n, N = len(A), 1 << len(A)

        w = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(min(len(A[i]), len(A[j])), 0, -1):
                    if A[j].startswith(A[i][-k:]):
                        w[i][j] = k
                        break

        f = [[None] * n for _ in range(N)]
        for i in range(N):
            for k in filter(lambda x: (1 << x) & i, range(n)):
                i1 = i ^ (1 << k)
                f[i][k] = min([f[i1][j] + A[k][w[j][k]:]
                               for j in filter(lambda x: (1 << x) & i1, range(n))],
                              key=len, default=A[k])

        return min(filter(None, f[-1]), key=len)
