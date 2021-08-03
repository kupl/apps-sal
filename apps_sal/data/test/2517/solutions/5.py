# ABC073 D - joisino's travel
from scipy.sparse.csgraph import floyd_warshall
from itertools import permutations

N, M, R = map(int, input().split())
r = list(map(int, input().split()))

inf = 10**18
dist = [[inf] * N for _ in range(N)]
for i in range(M):
    A, B, C = map(int, input().split())
    dist[A - 1][B - 1] = dist[B - 1][A - 1] = C

dist = floyd_warshall(dist)

ans = inf
for rr in permutations(r):
    cost = 0
    for i in range(R - 1):
        cost += dist[rr[i] - 1][rr[i + 1] - 1]
    if cost < ans:
        ans = cost
print(int(ans))
