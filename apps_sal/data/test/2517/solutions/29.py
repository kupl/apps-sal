from itertools import permutations
from scipy.sparse.csgraph import floyd_warshall
INF = 1001001001
(N, M, R) = list(map(int, input().split()))
r = list(map(int, input().split()))
graph = [[INF] * N for _ in range(N)]
for i in range(M):
    (A, B, C) = list(map(int, input().split()))
    graph[A - 1][B - 1] = C
    graph[B - 1][A - 1] = C
dist_matrix = floyd_warshall(graph)
ans = INF
for root in permutations(r):
    cnt = 0
    for j in range(R - 1):
        cnt += dist_matrix[root[j] - 1][root[j + 1] - 1]
    ans = min(ans, cnt)
print(int(ans))
