from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix
(h, w) = map(int, input().split())
ma = [list(map(int, input().split(' '))) for i in range(10)]
sco = [list(map(int, input().split(' '))) for i in range(h)]
a = csr_matrix(ma)
b = dijkstra(a)
ans = 0
for i in range(h):
    for j in range(w):
        num = sco[i][j]
        if num != -1:
            ans += b[num][1]
print(int(ans))
