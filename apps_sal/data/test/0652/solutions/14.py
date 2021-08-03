p, d = [], {}
for i in range(int(input())):
    x, y = list(map(int, input().split()))
    for a, b in p:
        u, v = a - x, b - y
        q = (u / v if v else int(2e9), u * u + v * v)
        d[q] = d.get(q, 0) + 1
    p.append((x, y))
print(sum(k * k - k for k in list(d.values())) // 4)
