def f():
    return map(int, input().split())


(n, k) = f()
t = {k ** i for i in range(48) if k ** i <= n * 1000000000.0}
s = y = 0
d = {0: 1}
for a in f():
    s += a
    d[s] = d.get(s, 0) + 1
    y += sum((d.get(s - x, 0) for x in t))
print(y)
