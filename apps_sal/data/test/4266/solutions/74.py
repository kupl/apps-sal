(k, n) = map(int, input().split())
arr = list(range(n - k + 1, n + k))
print(' '.join([str(n) for n in arr]))
