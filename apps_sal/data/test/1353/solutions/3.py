n, m, a, b = list(map(int, input().split()))
res = 10 ** 100

for i in range(10000):
    res = min(res, i * b + max(n - i * m, 0) * a)
print(res)
