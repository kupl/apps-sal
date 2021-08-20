(n, m) = map(int, input().split())
x = n // m
k = m - n % m
print(k * x * (x - 1) // 2 + (m - k) * (x + 1) * x // 2, (n - m + 1) * (n - m) // 2)
