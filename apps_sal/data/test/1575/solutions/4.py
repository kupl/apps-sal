def f(): return map(int, input().split())


a, b, t = f()
k, = f()
s = d = 1e12
for q in (f() if k else []):
    if q > a:
        s = a
    if q > a or a + t > b:
        break
    elif a - q < d:
        s, d = q - 1, a - q
    a += t
print(s if a + t > b else a)
