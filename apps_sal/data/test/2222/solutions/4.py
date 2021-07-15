n = int(input())
a = [None] + list(map(int, input().split()))
p = [None, None] + list(map(int, input().split()))

g = [[] for i in range(n + 1)]
for i in range(n, 0, -1):
    if g[i]:
        c = 0
        x, y = 0, 10 ** 9
        for cv, wv in g[i]:
            c += cv
            x += wv
            y = min(y, wv)
        w = y if a[i] else x
    else:
        c, w = 1, 1
    if i == 1:
        print(c - w + 1)
    else:
        g[p[i]].append((c, w))
