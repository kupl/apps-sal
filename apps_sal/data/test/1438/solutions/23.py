n, k = list(map(int, input().split()))
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [b[i] // a[i] for i in range(n)]
d = [b[i] % a[i] for i in range(n)]
while k:
    i = c.index(min(c))
    m = min(k, a[i] - d[i])
    d[i] += m
    k -= m
    c[i] += d[i] // a[i]
    d[i] %= a[i]
print(min(c))
