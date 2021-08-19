(n, x, *a) = map(int, open(0).read().split())
print(n + (x - sum(a)) // min(a))
