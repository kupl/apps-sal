(n, m) = map(int, input().split())
a = [int(input()) for i in range(m)]
d = [1] * (n + 1)
for i in range(m):
    d[a[i]] = 0
for i in range(2, n + 1):
    if d[i] != 0:
        d[i] = d[i - 1] + d[i - 2]
print(d[n] % (10 ** 9 + 7))
