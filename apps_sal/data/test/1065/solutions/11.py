n, k, m, d = list(map(int, input().split()))
res = 0
for i in range(1, d + 1):
    x = n // ((i - 1) * k + 1)
    x = min(x, m)
    if (x == 0):
        continue
    if ((((n // x) - 1) // k + 1) != i):
        continue
    res = max(res, i * x)
print(int(res))
