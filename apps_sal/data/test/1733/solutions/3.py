from collections import defaultdict
(n, x, y) = list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
chk = [False] * (n + 1)
cnt = [1] * (n + 1)
adj = defaultdict(list)
for (u, v) in edges:
    adj[u].append(v)
    adj[v].append(u)


def dfs(y, x, adj):
    vis = set()
    stk = [y]
    stack_order = []
    while stk:
        u = stk.pop()
        vis.add(u)
        if u == x:
            chk[u] = True
        order = []
        for v in adj[u]:
            if v not in vis:
                stk.append(v)
                order.append(v)
        if order:
            stack_order.append((u, order))
    while stack_order:
        u = stack_order.pop()
        for v in u[1]:
            cnt[u[0]] += cnt[v]
            chk[u[0]] |= chk[v]


dfs(y, x, adj)
res = 0
for i in adj[y]:
    if chk[i]:
        res = cnt[y] - cnt[i]
        break
print(n * (n - 1) - res * cnt[x])
