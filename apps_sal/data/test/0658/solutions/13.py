def f(): return map(int, input().split())


n, w, v, u = f()
k = t = 0
v /= u
for i in range(n):
    x, y = f()
    d = x / v - y
    k |= d < 0
    t = max(t, d)
if k:
    w += t
print(w / u)
