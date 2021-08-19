from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson, csgraph_from_dense
(H, W) = [int(x) for x in input().split()]
C = [[int(x) for x in input().split()] for _ in range(10)]
A = [[int(x) for x in input().split()] for _ in range(H)]
G = csgraph_from_dense(C, null_value=0)
d = floyd_warshall(G)
ans = 0
for i in range(H):
    for j in range(W):
        if A[i][j] == 1 or A[i][j] == -1:
            continue
        ans += d[A[i][j]][1]
print(int(ans))
