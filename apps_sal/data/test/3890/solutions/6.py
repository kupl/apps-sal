((n, k), mod) = (list(map(int, input().split())), 1000000007)
print(k ** (k - 1) % mod * ((n - k) ** (n - k) % mod) % mod)
