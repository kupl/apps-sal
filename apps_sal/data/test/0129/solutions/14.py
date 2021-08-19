(n, m, k, l) = map(int, input().split())
if m > n or (l + k + m - 1) // m * m > n:
    print(-1)
else:
    x = (l + k + m - 1) // m
    print(x)
