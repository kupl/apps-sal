(n, k) = list(map(int, input().split()))
k = min(k, n // 2)
print((2 * n - 2 * k - 1) * k)
