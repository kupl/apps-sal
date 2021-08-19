from bisect import bisect_left
n = int(input())
xy = []
X = []
Y = []
for _ in range(n):
    (x, y) = list(map(int, input().split()))
    xy.append([x, y])
    X.append(x)
    Y.append(y)
X = list(set(X))
Y = list(set(Y))
X.sort()
Y.sort()
xy = [[bisect_left(X, x), bisect_left(Y, y)] for (x, y) in xy]
mx = 0
my = 0
for (x, y) in xy:
    mx = max(mx, x)
    my = max(my, y)
(mx, my) = (mx + 1, my + 1)
bg = [[] for _ in range(mx + my)]
for (x, y) in xy:
    y += mx
    bg[x].append(y)
    bg[y].append(x)
mi = set(range(mx + my))
ren = []
while mi:
    todo = [mi.pop()]
    (rx, ry) = (0, 0)
    while todo:
        v = todo.pop()
        if v < mx:
            rx += 1
        else:
            ry += 1
        for nv in bg[v]:
            if nv in mi:
                todo.append(nv)
                mi.discard(nv)
    ren.append([rx, ry])
ans = 0
for (rx, ry) in ren:
    ans += rx * ry
ans -= n
print(ans)
