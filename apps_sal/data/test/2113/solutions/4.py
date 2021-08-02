n = int(input())
g = [[] for i in range(n)]
for i in range(n - 1):
    u, v = map(int, input().split())
    g[u - 1].append(v - 1)
    g[v - 1].append(u - 1)

q = [[0, 0]]
lvls = [0 for i in range(n)]
lvls[0] = 1
vis = set([0])
while len(q) > 0:
    v = q[0][0]
    l = q[0][1]
    del q[0]
    for u in g[v]:
        if u not in vis:
            vis.add(u)
            q.append([u, l + 1])
            lvls[l + 1] += 1

clvls = [i for i in lvls]
for i in range(2, n):
    if lvls[i] == 0:
        break
    clvls[i] += clvls[i - 2]
ans = 0
for i in range(2, n):
    if lvls[i] == 0:
        break
    ans += lvls[i] * (clvls[i - 1] - 1)

print(ans)
