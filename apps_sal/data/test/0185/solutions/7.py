n, k = list(map(int, input().split()))
print(n * 3 + min(k, n + 1 - k) - 1)
