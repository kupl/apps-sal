(n, w, v, u) = list(map(int, input().split()))
v = u / v
l = r = 0
for _ in range(n):
    (x, y) = list(map(int, input().split()))
    y -= v * x
    l = min(l, y)
    r = max(r, y)
print((w - (l if r else 0)) / u)
