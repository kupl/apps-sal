from itertools import permutations
from scipy.sparse.csgraph import floyd_warshall
n, m, r = map(int, input().split())
vis = list(map(int, input().split()))
INF = 10**18
path = [[INF] * n for i in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    path[a - 1][b - 1] = c
    path[b - 1][a - 1] = c
path = floyd_warshall(path)
ans = 10**18
for root in permutations(vis):
    cnt = 0
    for j in range(1, r):
        cnt += path[root[j - 1] - 1][root[j] - 1]
    ans = min(ans, cnt)
print(int(ans))
