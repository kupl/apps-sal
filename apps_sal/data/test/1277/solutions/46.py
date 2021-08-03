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

prev = [-1] * N


def dfs(v, p=-1):
    for to in es[v]:
        if to == p:
            continue
        prev[to] = v
        dfs(to, v)


dfs(U)

path = [V]
while prev[path[-1]] >= 0:
    path.append(prev[path[-1]])
ban = set(path[:(len(path) + 1) // 2])

reach = [0] * N
reach[U] = 1


def dfs2(v, p=-1):
    for to in es[v]:
        if to == p:
            continue
        if to in ban:
            continue
        reach[to] = 1
        dfs2(to, v)


dfs2(U)

depth = [0] * N
ans = 0


def dfs3(v, p=-1):
    nonlocal ans
    for to in es[v]:
        if to == p:
            continue
        depth[to] = depth[v] + 1
        if reach[to]:
            ans = max(ans, depth[v])
        dfs3(to, v)


dfs3(V)

print(ans)
