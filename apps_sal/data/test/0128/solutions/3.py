
n, k = list(map(int, input().split()))

k = min(k, n // 2)
print(k * (n - k) + (n - 2 * k) * k + k * (k - 1))
