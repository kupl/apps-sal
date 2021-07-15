n, m = map(int, input().split())
k, d = n // m, n % m
print((str(k) + ' ') * (m - d) + (str(k + 1) + ' ') * d)
