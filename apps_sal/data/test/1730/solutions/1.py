n, l, k = map(int, input().split())
c = list([] for i in range(n + 1))
for i in range(l):
    x, y = map(int, input().split())
    c[x].append(y)
    c[y].append(x)
d = list(0 for i in range(n + 1))
d[1] = 1
now = 1
time = 1
f = True
while f:
    time += 1
    v = 0
    while v >= 0:
        if d[c[now][v]] == 0:
            now = c[now][v]
            d[now] = time
            v = -1
        elif d[c[now][v]] + k < time:
            f = False
            mintime = d[c[now][v]]
            v = -1
        else:
            v += 1
g = list(0 for i in range(time - mintime))
for i in range(n + 1):
    if d[i] >= mintime:
        g[d[i] - mintime] = i
print(time - mintime)
print(*g)
