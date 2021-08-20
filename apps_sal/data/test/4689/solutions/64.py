(k, n) = map(int, input().split())
a = [int(s) for s in input().split()]
d = [0] * (n + 1)
d[0] = a[0] - 0
for i in range(1, n):
    d[i] = a[i] - a[i - 1]
d[n] = k - a[n - 1] + a[0]
print(k - max(d))
