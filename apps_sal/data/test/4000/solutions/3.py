import sys
from collections import deque
n = int(input())
adj = [[] for _ in range(n)]
for (u, v) in (list(map(int, l.split())) for l in sys.stdin):
    adj[u - 1].append(v - 1)
    adj[v - 1].append(u - 1)
inf = 10 ** 9


def rec(s):
    prev = [-1] * n
    prev[s] = inf
    dq = deque([s])
    last = s
    while dq:
        v = dq.popleft()
        last = v
        for dest in adj[v]:
            if prev[dest] > -1:
                continue
            prev[dest] = v
            dq.append(dest)
    return (last, prev)


(v1, _) = rec(0)
(v2, prev) = rec(v1)
v = prev[v2]
visited = [0] * n
visited[v] = visited[v1] = visited[v2] = 1
dia = 0
(max_e, max_e_i) = (0, v)
while v != inf:
    dia += 1
    if prev[v] != inf:
        visited[prev[v]] = 1
    stack = [(v, 0)]
    while stack:
        (cv, e) = stack.pop()
        if max_e < e:
            (max_e, max_e_i) = (e, cv)
        e += 1
        for dest in adj[cv]:
            if visited[dest]:
                continue
            visited[dest] = 1
            stack.append((dest, e))
    v = prev[v]
print(dia + max_e)
print(v1 + 1, v2 + 1, max_e_i + 1)
