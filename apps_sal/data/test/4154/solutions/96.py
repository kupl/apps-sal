(n, m, *lr) = list(map(int, open(0).read().split()))
print(max(0, min(lr[1::2]) - max(lr[::2]) + 1))
