n, k = list(map(int, input().split()))

print(min(n - k, min(k, 1)), min(2 * k, n - k))
