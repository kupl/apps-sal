n, m = list(map(int, input().split()))
if n < m:
    print(-1)
else:
    k = (n + 2 * m - 1) // (2 * m)
    x = n - k * m
    y = 2 * k * m - n
    print(x + y)
