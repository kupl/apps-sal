n, L = [int(x) for x in input().split()]
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s1 = a[n - 1]
s2 = b[n - 1]
x1 = L - s1
x2 = L - s2
c = []
d = []
c.append(a[0] + x1)
d.append(b[0] + x2)
for i in range(n - 1):
    c.append(a[i + 1] - a[i])
    d.append(b[i + 1] - b[i])
for i in range(n):
    k = True
    for j in range(n):
        if c[j] != d[(j + i) % n]:
            k = False
    if (k):
        print("YES")
        return
print("NO")

