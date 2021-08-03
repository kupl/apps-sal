n, m = map(int, input().split())
if n * m == 1:
    print(1)
else:
    print(1 / n + (n - 1) * (m - 1) / (n * (n * m - 1)))
