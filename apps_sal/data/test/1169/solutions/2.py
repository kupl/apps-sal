(n, m) = map(int, input().split())
l = 0
r = n
for i in range(50):
    md = (l + r) // 2
    if md * (md - 1) // 2 < m:
        l = md
    else:
        r = md
print(max(0, n - m * 2), n - r)
