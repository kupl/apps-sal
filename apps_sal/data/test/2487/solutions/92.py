(n, *l) = map(int, open(0).read().split())
n += 1
i = iter(l)
print((n ** 3 - n) // 6 - sum((min(u, v) * (n - max(u, v)) for (u, v) in zip(i, i))))
