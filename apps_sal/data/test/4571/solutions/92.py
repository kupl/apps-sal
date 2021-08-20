(n, m) = map(int, input().split())
t = 2 ** m
print((m * 1900 + (n - m) * 100) * t)
