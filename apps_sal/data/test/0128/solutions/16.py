(n, k) = [int(s) for s in input().split()]
k = min(n // 2, k)
print((2 * n - 2 * k - 1) * k)
