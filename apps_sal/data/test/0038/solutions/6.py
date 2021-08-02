n, l = list(map(int, input().split()))
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
c = [0] * n
d = [0] * n
for i in range(n - 1):
    c[i] = a[i + 1] - a[i]
c[n - 1] = l - sum(c)

for i in range(n - 1):
    d[i] = b[i + 1] - b[i]
d[n - 1] = l - sum(d)


f = False
for i in range(0, n):
    if d == c[i:n] + c[:i]:
        f = True

if f:
    print("YES")
else:
    print("NO")
