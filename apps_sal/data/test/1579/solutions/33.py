n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
maxx = max([x for (x, y) in xy])
maxy = max([y for (x, y) in xy])
g = [[] for _ in range(maxx + maxy + 1)]
for (x, y) in xy:
    y += maxx
    g[x].append(y)
    g[y].append(x)
mi = set(range(maxx + maxy + 1))
ans = 0
while mi:
    v = mi.pop()
    todo = [v]
    nx = 0
    ny = 0
    while todo:
        v = todo.pop()
        if v <= maxx:
            nx += 1
        else:
            ny += 1
        for nv in g[v]:
            if nv in mi:
                mi.discard(nv)
                todo.append(nv)
    ans += nx * ny
print(ans - n)
