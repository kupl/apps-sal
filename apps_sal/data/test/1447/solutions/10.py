(n, m) = map(float, input().split())
if n == 1 and m == 1:
    print(1)
else:
    print(1 / n + (n - 1) * (m - 1) / n / (n * m - 1))
