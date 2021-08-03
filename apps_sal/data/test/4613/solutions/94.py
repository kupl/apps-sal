from collections import deque
import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())
bridges = [None] * M
G = [[] for i in range(N)]

for i in range(M):
    a, b = map(int, readline().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
    bridges[i] = (a - 1, b - 1)


ans = 0
for i in range(M):
    q = deque([])
    q.append(0)
    seen = set()
    while q:
        v = q.popleft()
        if v in seen:
            continue
        seen.add(v)
        for child in G[v]:
            if (v, child) == bridges[i] or (child, v) == bridges[i]:
                continue
            q.append(child)
    if len(seen) != N:
        ans += 1

print(ans)
