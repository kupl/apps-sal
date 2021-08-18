n, s, v1, v2, k = map(int, input().split())
n = (n + k - 1) // k
l, r, m = 0, 1000000000000000000, 0
for _ in range(300):
    m = (l + r) / 2
    y = (s - v1 * m) / (v2 - v1)
    gap = y * (v2 - v1)
    pikap = gap / (v1 + v2)
    if pikap * (n - 1) + n * y <= m:
        r = m
    else:
        l = m
print("%.10f" % r)
