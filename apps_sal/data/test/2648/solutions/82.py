(n, *a) = map(int, open(0).read().split())
k = len(set(a))
print(k - (n - k) % 2)
