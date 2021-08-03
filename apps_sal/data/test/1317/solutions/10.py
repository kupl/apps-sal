n, m = map(int, input().split())
a = [0 for i in range(m)]
for i in range(m):
    a[i] = n // m
for i in range(1, n % m + 1):
    a[i] += 1
res = 0
for i in range(m):
    for j in range(m):
        if ((i * i + j * j) % m == 0):
            res += a[i] * a[j]
print(res)
