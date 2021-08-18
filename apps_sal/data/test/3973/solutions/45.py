n, m = map(int, input().split())
a = list(map(int, input().split()))
a = [b - 1 for b in a]
imos = [0 for _ in range(m + 1)]
base = 0
for i in range(n - 1):
    x, y = a[i], a[i + 1]
    if y - x == 1 or x + 1 - m == y:
        continue
    z, w = (x + 2) % m, (y + 1) % m
    if w == 0:
        w = m
    if z < w:
        imos[z] += 1
        imos[w] -= w - z + 1
        if w < m:
            imos[w + 1] += w - z
    else:
        imos[z] += 1
        imos[m] -= m - z + 1
        imos[0] += 1
        base += m - z
        imos[w] -= m + w - z + 1
        if w < m:
            imos[w + 1] += m + w - z
for i in range(m):
    imos[i + 1] += imos[i]
imos[0] += base
for i in range(m):
    imos[i + 1] += imos[i]
res = max(imos[:m])
ans = 0
for i in range(n - 1):
    if a[i + 1] > a[i]:
        ans += a[i + 1] - a[i]
    else:
        ans += a[i + 1] + m - a[i]
ans -= res
print(ans)
