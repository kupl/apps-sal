import sys
rd = sys.stdin.readline
sys.setrecursionlimit(10000000)
(n, T, A) = map(int, rd().split())
(T, A) = (T - 1, A - 1)
graph = [[] for _ in range(n)]
for i in range(n - 1):
    (a, b) = map(int, rd().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)


def dfs(v, p=-1):
    deg = len(graph[v])
    if v == T:
        root.append(v)
        return True
    if deg == 1 and v != A:
        return False
    ok = False
    for i in range(deg):
        u = graph[v][i]
        if u == p:
            continue
        if dfs(u, v):
            root.append(v)
            ok = True
    return ok


def dfs2(v, p=-1):
    deg = len(graph[v])
    if deg == 1 and v != root[x]:
        return 0
    depth = 0
    for i in range(deg):
        u = graph[v][i]
        if u == p:
            continue
        d = dfs2(u, v)
        depth = max(depth, d + 1)
    return depth


root = []
dfs(A)
x = len(root) // 2 - 1
dp = [0] * n
ans = len(root) // 2 + dfs2(root[x], root[x + 1])
if len(root) % 2 == 0:
    ans -= 1
print(ans)
