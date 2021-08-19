(n, m) = map(int, input().split())
a = sorted([list(map(int, input().split())) for i in range(n)])
c = 0
d = 0
for i in range(n):
    if c + a[i][1] <= m:
        c += a[i][1]
        d += a[i][0] * a[i][1]
    else:
        d += (m - c) * a[i][0]
        break
print(d)
