from scipy.sparse.csgraph import floyd_warshall

N, M = map(int, input().split())

edge = [[float("inf") for i in range(N)] for j in range(N)]

abc = []
for _ in range(M):
    a, b, c = map(int, input().split())
    abc.append((a, b, c))
    edge[a - 1][b - 1] = c
    edge[b - 1][a - 1] = c

dist = floyd_warshall(edge)

ans = 0

for a, b, c in abc:
    if dist[a - 1][b - 1] != c:
        ans += 1

print(ans)
