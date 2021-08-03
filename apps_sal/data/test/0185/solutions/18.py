n, k = list(map(int, input().split()))

mn = min(k - 1, n - k)

print(3 * n + mn)
