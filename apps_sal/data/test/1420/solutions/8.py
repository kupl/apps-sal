n, l = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
res = 0
d = [0] * (n + 1)

a.sort()

d[0] = a[0]
d[n] = l - a[n - 1]
for i in range(1, n):
    d[i] = (a[i] - a[i - 1]) / 2

for i in range(n + 1):
    res = max(res, d[i])

print(res)

