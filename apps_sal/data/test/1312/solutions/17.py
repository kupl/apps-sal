n, m = list(map(int, input().split()))
q, r = divmod(n, m)
print(' '.join(map(str, [q] * (m - r) + [q + 1] * r)))
