f = lambda: list(map(int, input().split()))
n, m, k = f()
s = d = 0
for t in zip(*[f() for i in range(n)]):
    p, q = x, y = sum(t[:k]), 0
    for j in range(n - k):
        p += t[j + k] - t[j]
        q += t[j]
        if p > x: x, y = p, q
    s += x
    d += y
print(s, d)
