def f():
    return map(int, input().split())


(n, w, v, u) = f()
k = 0
d = t = w / u
for i in range(n):
    (x, y) = f()
    (a, b) = (x / v, y / u)
    k |= a < b
    t = max(t, a + d - b)
print([d, t][k])
