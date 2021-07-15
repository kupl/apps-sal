INF = float("inf")

def WarshallFloyd(M):
    N = len(M)
    for k in range(N):
        for j in range(N):
            for i in range(N):
                M[i][j] = min(M[i][j], M[i][k] + M[k][j])
    return M


N, M, *ABC = map(int, open(0).read().split())

E = [[INF] * (N + 1) for _ in range(N + 1)]
for a, b, c in zip(*[iter(ABC)] * 3):
    E[a][b] = c
    E[b][a] = c

D = WarshallFloyd(E)

print(sum(D[a][b] < c for a, b, c in zip(*[iter(ABC)] * 3)))
