def f():
    return map(int, input().split())


(n, m, k) = f()
s = d = 0
for t in zip(*[f() for i in range(n)]):
    (p, q) = (x, y) = (sum(t[:k]), 0)
    for (a, b) in zip(t[:n - k], t[k:]):
        p += b - a
        q += a
        if p > x:
            (x, y) = (p, q)
    s += x
    d += y
print(s, d)
