a, b, x = map(int, input().split())
ls = []
for i in range(1, 10):
    l, r = 10**(i - 1), 10**i - 1
    y = (x - b * i) // a
    for _ in range(10000):
        m = (l + r) / 2
        if y == m:
            break
        elif y < m:
            r = m
        else:
            l = m
    m = round(m)
    for n in [m - 1, m, m + 1]:
        if a * n + b * len(str(n)) <= x:
            ls.append(n)
print(max(ls) if ls else 0)
