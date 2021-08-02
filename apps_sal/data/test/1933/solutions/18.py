n, m, k = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
v = []
for i in range(m):
    v.append([])
    x = 0
    for j in range(n):
        if a[j][i] == 1:
            s = 0
            for o in range(min(k, n - j)):
                s += a[j + o][i]
            v[i].append((s, n - x))
            x += 1
x, y = 0, 0
for i in range(len(v)):
    v[i].sort()
    if len(v[i]) > 0:
        x += v[i][-1][0]
        y += n - v[i][-1][1]
print(x, y)
