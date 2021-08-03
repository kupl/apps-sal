n, k, x, y = [int(input()) for _ in range(4)]
print((min(n, k) * x + max(0, n - k) * y))
