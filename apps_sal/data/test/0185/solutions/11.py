n, k = map(int, input().split())
print(n + min(k - 1, n - k) + n + n)
