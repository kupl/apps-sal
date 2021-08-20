(n, m) = map(int, input().split())
x = n // m
y = n % m
print(' '.join([str(x + 1)] * y + [str(x)] * (m - y)))
