m, n = map(int, input().split())

if m == 1:
    print(1)
else:
    print(1 / m + (n - 1) * (m - 1) / (m * (m * n - 1)))
