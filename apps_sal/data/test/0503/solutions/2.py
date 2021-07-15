n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
z = dict()
s = 0
for i in range(n):
    if not a[i] in z:
        z[a[i]] = [0, 0, 0]
    if a[i] % (k * k) == 0 and a[i] // k in z:
        q = z[a[i] // k][1]
        z[a[i]][2] += z[a[i] // k][1]
        s += q
    if a[i] % k == 0 and a[i] // k in z:
        z[a[i]][1] += z[a[i] // k][0]
    z[a[i]][0] += 1
print(s)

