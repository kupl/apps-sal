from scipy.sparse.csgraph import floyd_warshall
'\ndef warshall_floyd(d):\n    for k in range(N):\n        for i in range(N):\n            for j in range(N):\n                d[i][j] =min(d[i][j],d[i][k] + d[k][j])            \n    return d\n'
(N, M, L) = map(int, input().split())
d = [[0 for i in range(N)] for i in range(N)]
for i in range(M):
    (A, B, C) = map(int, input().split())
    d[A - 1][B - 1] = C
    d[B - 1][A - 1] = C
d = floyd_warshall(d, directed=False)
S = [[0 for i in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        if d[i][j] <= L:
            S[i][j] = 1
            S[j][i] = 1
S = floyd_warshall(S, directed=False)
Q = int(input())
for i in range(Q):
    (s, t) = map(int, input().split())
    if S[s - 1][t - 1] == float('inf'):
        print(-1)
    else:
        print(int(S[s - 1][t - 1] - 1))
