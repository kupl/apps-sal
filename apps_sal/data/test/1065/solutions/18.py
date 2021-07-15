n, k, m, d = [int(x) for x in input().split()]
res = 0
for a in range(1, d + 1):
    x = n // (a * k - k + 1)
    x = min(x, m)
    res = max(res, x * a)
print(res)
