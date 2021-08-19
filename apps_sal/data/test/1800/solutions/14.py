(a, b) = (int(i) for i in input().split())
f = list(map(int, input().split()))
d = []
for i in range(b):
    (c, e) = (int(t) for t in input().split())
    while len(d) > 0 and e > d[-1][1]:
        d.pop()
    d.append([c, e])
(c, e) = (0, d[0][1])
d.append([0, 0])
g = sorted(f[:e])
for i in range(1, len(d)):
    for y in range(d[i - 1][1], d[i][1], -1):
        if d[i - 1][0] == 1:
            f[y - 1] = g[e - 1]
            e -= 1
        else:
            f[y - 1] = g[c]
            c += 1
for i in range(len(f)):
    print(f[i], end=' ')
