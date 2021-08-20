import sys
[n, m, s1, t1] = list(map(int, sys.stdin.readline().strip().split()))
(s, t) = (s1 - 1, t1 - 1)
tos = [[] for _ in range(n)]
for _ in range(m):
    [u1, v1] = list(map(int, sys.stdin.readline().strip().split()))
    (v, u) = (v1 - 1, u1 - 1)
    tos[v].append(u)
    tos[u].append(v)


def S_l(v0, tos):
    n = len(tos)
    visited = [False for _ in range(n)]
    visited[v0] = True
    queue = [v0]
    hq = 0
    l = [0 for _ in range(n)]
    while len(queue) > hq:
        u = queue[hq]
        hq += 1
        for v in tos[u]:
            if not visited[v]:
                l[v] = l[u] + 1
                queue.append(v)
                visited[v] = True
    return l


lt = S_l(t, tos)
ls = S_l(s, tos)
d = lt[s]
count = 0
for u in range(n):
    for v in range(u):
        if v not in tos[u] and min(lt[u] + ls[v], lt[v] + ls[u]) + 1 >= d:
            count += 1
print(count)
