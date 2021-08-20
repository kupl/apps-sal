import sys


def input():
    return sys.stdin.readline().rstrip()


sys.setrecursionlimit(50000)


def scc(N, G, RG):
    order = []
    used = [0] * N
    group = [None] * N

    def dfs(s):
        used[s] = 1
        for t in G[s]:
            if not used[t]:
                dfs(t)
        order.append(s)

    def rdfs(s, col):
        group[s] = col
        used[s] = 1
        for t in RG[s]:
            if not used[t]:
                rdfs(t, col)
    for i in range(N):
        if not used[i]:
            dfs(i)
    used = [0] * N
    label = 0
    for s in reversed(order):
        if not used[s]:
            rdfs(s, label)
            label += 1
    return (label, group)


def construct(N, G, label, group):
    G0 = [[] for i in range(label)]
    GP = [[] for i in range(label)]
    for v in range(N):
        lbs = group[v]
        for w in G[v]:
            lbt = group[w]
            if lbs == lbt:
                continue
            G0[lbs].append(lbt)
        GP[lbs].append(v)
    return (G0, GP)


(n, m, s) = map(int, input().split())
s -= 1
edge = [[] for _ in range(n)]
redge = [[] for _ in range(n)]
for _ in range(m):
    (a, b) = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    redge[b].append(a)
(label, group) = scc(n, edge, redge)
(a, b) = construct(n, redge, label, group)
ans = 0
for i in range(label):
    if len(a[i]) == 0:
        ans += i != group[s]
print(ans)
