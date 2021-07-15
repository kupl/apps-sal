#https://atcoder.jp/contests/abc075/submissions/15509548

n, m = list(map(int, input().split()))
g = [[] for _ in range(n)]
for i in range(m):
    a, b = list(map(int, input().split()))
    a, b = a-1, b-1
    g[a].append(b)
    g[b].append(a)

def lowlink(g, root=0):
    n = len(g)
    order = [n]*n
    low = [n]*n

    s = [root]
    cnt = 0
    par = [-1]*n
    seq = []
    while s:
        v = s.pop()
        if order[v] != n:
            continue
        order[v] = cnt
        seq.append(v)
        low[v] = cnt
        cnt += 1
        for u in g[v]:
            if order[u] < cnt:
                if par[v] != u:
                    low[v] = min(low[v], order[u])
                    continue
            else:
                par[u] = v
                s.append(u)
    child = [[] for _ in range(n)]
    for v in range(n):
        if par[v] != -1:
            child[par[v]].append(v)
    seq.reverse()
    for v in seq:
        for u in child[v]:
            low[v] = min(low[v], low[u])
    # bridge
    bridge = []
    for p in range(n):
        for c in child[p]:
            if order[p] < low[c]:
                bridge.append((p, c))

    # articulation points
    AP = []
    for v in range(n):
        if v == root:
            if len(child[v]) >= 2:
                AP.append(v)
        else:
            for c in child[v]:
                if order[v] <= low[c]:
                    AP.append(v)
                    break
    return AP, bridge

_, bridge = lowlink(g, 0)
print((len(bridge)))

