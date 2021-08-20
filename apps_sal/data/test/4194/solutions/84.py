(n, m, *a) = map(int, open(0).read().split())
print(max(n - sum(a), -1))
