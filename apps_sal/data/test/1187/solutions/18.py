v_n, e_n = tuple(map(int, input().split()))
G = [set() for _ in range(v_n)]
edges = []
d_s = [-1] * v_n
ok = False


def dfs(u):
    nonlocal ok
    if ok:
        return
    d_s[u] = 0
    for v in G[u]:
        if d_s[v] == -1:
            dfs(v)
        elif d_s[v] == 0:
            ok = True
    d_s[u] = 1


for _ in range(e_n):
    u, v = tuple(map(int, input().split()))
    u -= 1
    v -= 1
    edges.append((u, v))
    G[u].add(v)


for u in range(v_n):
    if d_s[u] == -1:
        dfs(u)


if not ok:
    print(1)
    for _ in range(e_n):
        print(1, end=' ')
else:
    print(2)
    for (u, v) in edges:
        print(int(u < v) + 1, end=' ')
