n, *a = map(int, open(0).read().split())
a = sorted([(j, i) for i, j in enumerate(a)], reverse=True)
dp = [0]
for i, (j, k) in enumerate(a):
    ldp = [abs(k - i + a) * j + b for a, b in enumerate(dp)]
    rdp = [abs(n - 1 - k - a) * j + b for a, b in enumerate(dp)]
    dp = [max(a, b) for a, b in zip(ldp + [0], [0] + rdp)]
print(max(dp))
