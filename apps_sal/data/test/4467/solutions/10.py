from collections import defaultdict
from itertools import product
N = int(input())
red_points = [tuple(map(int, input().split(' '))) for _ in range(N)]
blue_points = [tuple(map(int, input().split(' '))) for _ in range(N)]
edges = defaultdict(set)
for (i, j) in product(list(range(N)), repeat=2):
    (a, b) = red_points[i]
    (c, d) = blue_points[j]
    if a < c and b < d:
        edges[i].add(j + N)
        edges[j + N].add(i)
pairs = [-1] * (2 * N)
ans = 0


def dfs(v, seen):
    seen[v] = True
    for u in edges[v]:
        w = pairs[u]
        if w < 0 or (not seen[w] and dfs(w, seen)):
            pairs[v] = u
            pairs[u] = v
            return True
    return False


for v in range(2 * N):
    if pairs[v] < 0:
        seen = [False] * (2 * N)
        if dfs(v, seen):
            ans += 1
print(ans)
