N = int(input())
d = {}
for i in range(1, 10):
    for j in range(1, 10):
        d[i * 10 + j] = 0
for i in range(1, min(10, N + 1)):
    d[i * 10 + i] = 1
p, h, t, c = 10, 10, 1, 1
for i in range(11, N + 1):
    if t == 10:
        t = 1
    else:
        d[h + t] += 1
        t += 1
    if p == c:
        h += 10
        c = 0
    if h == 100:
        h = 10
        p *= 10
    c += 1
ans = 0
for i in range(1, 9):
    for j in range(i + 1, 10):
        ans += (d[i * 10 + j] * d[j * 10 + i]) * 2
for i in range(1, 10):
    ans += d[i * 10 + i]**2
print(ans)
