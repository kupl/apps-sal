n, w = list(map(int, input().split()))
x1, y1 = list(map(int, input().split()))
d = {x1: [y1], x1 + 1: [], x1 + 2: [], x1 + 3: []}
for _ in range(n - 1):
    x, y = list(map(int, input().split()))
    d[x].append(y)
d = {k: [0] + sorted(d[k], reverse=True) for k in d}
vm = 0
v1, w1 = 0, 0
for e in d[x1]:
    v1 += e
    w1 += 0 if e == 0 else x1
    v2, w2 = 0, 0
    for f in d[x1 + 1]:
        v2 += f
        w2 += 0 if f == 0 else x1 + 1
        v3, w3 = 0, 0
        for g in d[x1 + 2]:
            v3 += g
            w3 += 0 if g == 0 else x1 + 2
            v4, w4 = 0, 0
            for h in d[x1 + 3]:
                v4 += h
                w4 += 0 if h == 0 else x1 + 3
                ws = w1 + w2 + w3 + w4
                vs = v1 + v2 + v3 + v4
                if ws <= w:
                    vm = max(vm, vs)
print(vm)
