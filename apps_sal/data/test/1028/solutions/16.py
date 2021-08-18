3

n, m = list(map(int, input().split()))

k1 = (n - m + 1) * (n - m) // 2

div = n // m
mod = n % m

k2 = (m - mod) * div * (div - 1) // 2 + mod * (div + 1) * div // 2

print(min(k1, k2), max(k1, k2))
