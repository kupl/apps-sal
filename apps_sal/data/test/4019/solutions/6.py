[n, m, d] = list(map(int, input().split()))
g = {}
for i in range(n):
    g[i + 1] = set()
for i in range(m):
    [v, u] = list(map(int, input().split()))
    g[u].add(v)
    g[v].add(u)
seen = set()
comps = set()
for node in g[1]:
    if node in seen:
        continue
    comps.add(node)
    seen.add(node)
    q = [node]
    while len(q) > 0:
        v = q.pop()
        for to in g[v]:
            if to in seen or to == 1:
                continue
            q.append(to)
            seen.add(to)
if d > len(g[1]) or d < len(comps):
    print("NO")
else:
    print("YES")
    rem = 0
    rem2 = []
    for i in g[1]:
        if len(g[1]) - rem == d:
            break
        if i not in comps:
            rem2.append(i)
            rem += 1
    for i in rem2:
        g[1].discard(i)
    seen.clear()
    q = [1]
    while len(q) > 0:
        v = q.pop()
        discard = []
        for to in g[v]:
            if to in seen or to == 1:
                continue
            q.append(to)
            seen.add(to)
            print(v, " ", to)
