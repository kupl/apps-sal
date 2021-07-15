n, m = list(map(int, input().split()))

ans = 0

if n == 0:
    print((int(m * (m - 1) / 2)))
    return

if m == 0:
    print((int(n * (n - 1) / 2)))
    return

ans = (n * (n - 1) / 2) + (m * (m - 1) / 2)
print((int(ans)))

