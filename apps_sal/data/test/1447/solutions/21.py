n, m = map(int, input().split())

print(1 if n * m == 1 else 1 / n + (n - 1) / n * (m - 1) / (n * m - 1))
