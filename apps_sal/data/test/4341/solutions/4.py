n,m = [int(s) for s in input().split()]
g = [[] for x in range(n)]
for i in range(m):
    a,b = [int(s) for s in input().split()]
    g[a-1].append(b-1)
    g[b-1].append(a-1)
seen = [False for x in range(n)]
q = []
ans = 0
for i in range(len(g)):
    if not seen[i]:
        q.append(i)
        seen[i] = True
    is_cycle = True
    first = i
    cycle_len = 0
    while len(q) > 0:
        v = q.pop()
        cycle_len += 1
        if len(g[v]) != 2:
            is_cycle = False
        if len(g[v]) == 2 and (g[v][0] == first or g[v][1] == first) and cycle_len > 2 and is_cycle:
            ans += 1
            break
        for vv in g[v]:
            if not seen[vv]:
                q.append(vv)
                seen[vv] = True

print(ans)


