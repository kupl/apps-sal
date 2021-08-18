def dis(u, v):
    x1, y1 = u
    x2, y2 = v
    return(((x1 - x2)**2 + (y1 - y2)**2))


def adj(u):
    x, y = u
    t = []
    if x + 1 < n and a[x + 1][y] == '0':
        t.append([x + 1, y])
    if y + 1 < n and a[x][y + 1] == '0':
        t.append([x, y + 1])
    if x - 1 >= 0 and a[x - 1][y] == '0':
        t.append([x - 1, y])
    if y - 1 >= 0 and a[x][y - 1] == '0':
        t.append([x, y - 1])
    return(t)


def bfs(s):
    ans = [s]
    x, y = s
    v2[x][y] = 1
    frontier = [s]
    while frontier:
        nex = []
        for u in frontier:
            for v in adj(u):
                if v2[v[0]][v[1]] == 0:
                    nex.append(v)
                    v2[v[0]][v[1]] = 1
                    ans.append(v)
        frontier = nex
    return(ans)


n = int(input())
r1, c1 = [int(i) for i in input().split(' ')]
r2, c2 = [int(i) for i in input().split(' ')]
a = []
for i in range(n):
    a.append(list(input()))

v2 = [[0 for i in range(n)] for j in range(n)]

ans1 = bfs([r1 - 1, c1 - 1])
ans2 = bfs([r2 - 1, c2 - 1])
r = 9999999999
for i in ans1:
    for j in ans2:
        r = min(r, dis(i, j))
print(r)
