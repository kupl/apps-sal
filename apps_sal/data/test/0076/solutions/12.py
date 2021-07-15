n, m, a, b = map(int, input().split())

d = n % m
print(min(d * b, (m - d) * a))
