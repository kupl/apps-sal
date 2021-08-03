n = int(input())
d = {n: 0}
m = len(str(n)) + 1
u = int('1' * (m + 1))
for i in range(m, 0, -1):
    d, e, u = {}, d, u // 10
    for v, c in e.items():
        lim = v // u
        for x in range(-1 - lim, 1 - lim):
            t = v + x * u
            d[t] = min(c + i * abs(x), d.get(t, 999))
print(d[0])
