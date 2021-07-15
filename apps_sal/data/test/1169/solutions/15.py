n, m = list(map(int, input().split()))
l, r = 0, n
while l < r:
    c = (l + r) // 2
    if (c * (c - 1) // 2) < m:
        l = c + 1
    else:
        r = c
mn = 0
if m <= n // 2:
    mn = n - m * 2
print(mn, n - l)
