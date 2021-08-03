n = int(input())
es = list(map(int, input().split()))
g = [[] for i in range(n)]
for i, e in enumerate(es):
    g[i + 1].append(e - 1)
    g[e - 1].append(i + 1)
cols = list(map(int, input().split()))
ans = 0
q = [[0, 0]]
vis = set([0])
while len(q) > 0:
    v, c = q[0][0], q[0][1]
    del q[0]
    nc = cols[v]
    if nc != c:
        ans += 1
    for u in g[v]:
        if u not in vis:
            vis.add(u)
            q.append([u, nc])
print(ans)
