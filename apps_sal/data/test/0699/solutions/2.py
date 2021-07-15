y, k, n = map(int, input().split())
x = list(range(k - y % k, n - y + 1, k))
print(' '.join(str(i) for i in x) if x else -1)
