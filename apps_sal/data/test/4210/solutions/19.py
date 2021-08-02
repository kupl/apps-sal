n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
b = []
for i in range(11):
    c = {}
    for j in range(n):
        d = (a[j] * (10**i)) % k
        if d in c.keys():
            c[d] += 1
        else:
            c[d] = 1
    b.append(c)

s = 0
for i in range(n):
    c = a[i] % k
    d = (k - c) % k
    if d in b[len(str(a[i]))]:
        s += b[len(str(a[i]))][d]
    if (a[i] * (10**len(str(a[i])))) % k == d:
        s -= 1
print(s)
