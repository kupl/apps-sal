n, m = list(map(int, input().split()))
print(1.0 if n == m == 1 else 1 / n * ((n - 1) * (m - 1) / (n * m - 1) + 1))
