from scipy.sparse.csgraph import floyd_warshall
(N, M, L) = list(map(int, input().split()))
edges = [[0] * N for _ in range(N)]
for _ in range(M):
    (a, b, c) = list(map(int, input().split()))
    edges[a - 1][b - 1] = c
    edges[b - 1][a - 1] = c
Q = int(input())
st = []
for _ in range(Q):
    st.append([int(j) - 1 for j in input().split()])
edges = floyd_warshall(edges)
for i in range(N):
    for j in range(N):
        if edges[i][j] <= L:
            edges[i][j] = 1
        else:
            edges[i][j] = 0
edges = floyd_warshall(edges)
for (i, j) in st:
    if edges[i][j] == float('inf'):
        print(-1)
    else:
        print(int(edges[i][j]) - 1)
