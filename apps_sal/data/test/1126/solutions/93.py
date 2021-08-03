n, x, m = list(map(int, input().split()))

t, i, c, d = 0, 0, [0] * -~m, [0] * -~m
while i < n:
    i, t = i + 1, t + x
    c[x], d[i] = i, t
    x = x**2 % m
    if c[x]:
        break

if i != n and x != 0:
    p = c[x] - 1
    t = (d[i] - d[p]) * ((n - p) // (i - p)) + d[p + (n - p) % (i - p)]

print(t)
