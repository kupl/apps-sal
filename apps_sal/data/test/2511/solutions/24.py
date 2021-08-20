import sys
from collections import deque
mod = 10 ** 9 + 7
input = sys.stdin.readline
(N, K) = map(int, input().split())
paths = [[] for _ in range(N)]
for _ in range(N - 1):
    (a, b) = map(int, input().split())
    paths[a - 1].append(b - 1)
    paths[b - 1].append(a - 1)
q = deque()
q.append((0, K, 0))
dp = 1
visited = set()
while q:
    (node, count, d) = q.popleft()
    if node in visited:
        continue
    dp *= count
    dp %= mod
    visited.add(node)
    res = K
    if d == 0:
        res -= 1
    else:
        res -= 2
    for n_node in paths[node]:
        if n_node not in visited:
            q.append((n_node, res, d + 1))
            res -= 1
print(dp)
