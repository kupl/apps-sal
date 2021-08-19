(n, k1, k2) = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
d = [abs(a[i] - b[i]) for i in range(n)]
for i in range(k1):
    ind = d.index(max(d))
    d[ind] = abs(d[ind] - 1)
for i in range(k2):
    ind = d.index(max(d))
    d[ind] = abs(d[ind] - 1)
s = 0
for i in range(n):
    s += d[i] ** 2
print(s)
