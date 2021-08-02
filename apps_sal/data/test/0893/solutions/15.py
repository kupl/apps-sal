mod = 10**9 + 7
d, n = map(int, input().split())
a = [0] + list(map(int, input().split()))
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)


def dfs(u, root):
    visited[u] = True
    f[u] = 1
    for i in tree[u]:
        if visited[i] == False:
            if a[i] < a[root] or a[i] > a[root] + d: continue
            if a[i] == a[root] and i < root: continue
            dfs(i, root)
            f[u] = (f[u] * (f[i] + 1)) % (mod)


ans = 0
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    f = [0] * (n + 1)
    dfs(i, i)
    ans = (ans + f[i]) % mod
print(ans)
