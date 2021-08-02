n, m = map(int, input().split())
print(1.0 if n == m == 1 else ((n * m - n - m + 1) / (n * m - 1) + 1) / n)
