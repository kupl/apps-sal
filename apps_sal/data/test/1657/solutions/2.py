def f(): return map(int, input().split())


n, p = f()
s = [0] * n
x, y = -p, 0
for i in range(n):
    a, b = f()
    x += a
    y += b
    s[i] = (a, b)
s.sort(key=lambda q: q[0] / q[1])
for a, b in s:
    if b * x > a * y:
        x -= a
        y -= b
    else:
        break
print(y / x if x > 0 else -1)
