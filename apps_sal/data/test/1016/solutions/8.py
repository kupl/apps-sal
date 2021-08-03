used = set()


def dfs(v, root):
    nonlocal cnt
    if v in used:
        return
    used.add(v)
    for to in G[v]:
        dfs(to, root)
    if v == root:
        cnt += 1


cnt = 0
n, m = list(map(int, input().split()))
G = [[] for i in range(n)]

for i in range(m):
    x, y = list(map(int, input().split()))
    G[x - 1].append(y - 1)
    G[y - 1].append(x - 1)

for v in range(n):
    dfs(v, v)
print(2**(n - cnt))
