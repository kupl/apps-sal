(n, m) = map(int, input().split())
t = m * 1900 + (n - m) * 100
print(t * 2 ** m)
