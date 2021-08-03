import sys
sys.setrecursionlimit(10**8)
N, U, V = map(int, input().split())
U, V = U - 1, V - 1
AB = [tuple(map(int, input().split())) for i in range(N - 1)]
es = [[] for _ in range(N)]
for a, b in AB:
    a, b = a - 1, b - 1
    es[a].append(b)
    es[b].append(a)

dist1 = [N] * N
dist1[V] = 0


def dfs1(v, p=-1):
    for to in es[v]:
        if to == p:
            continue
        dist1[to] = dist1[v] + 1
        dfs1(to, v)


dfs1(V)

D = dist1[U]

dist2 = [N] * N
dist2[U] = 0


def dfs2(v, p=-1):
    for to in es[v]:
        if to == p:
            continue
        if (D + 1) // 2 > dist1[to]:
            continue
        dist2[to] = dist2[v] + 1
        dfs2(to, v)


dfs2(U)

ans = 0
for a, b in zip(dist1, dist2):
    if b == N:
        continue
    ans = max(ans, a - 1)
print(ans)
