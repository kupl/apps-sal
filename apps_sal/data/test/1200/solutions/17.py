from fractions import gcd
n = int(input())
a = input().split()
for i in range(0, n):
    a[i] = int(a[i])

a.sort()
dists = []
for i in range(1, n):
    dists.append(a[i] - a[i - 1])
s = dists[0]
gdc = dists[0]
for i in range(1, len(dists)):
    gdc = gcd(dists[i], gdc)
    s += dists[i]
print(s // gdc - n + 1)
