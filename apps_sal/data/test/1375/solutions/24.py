import bisect

n = int(input())
a = [int(x) for x in input().split()]
s, p, k = sum(a), a[0], sum(a) / 3
b, c = [], []
for i in range(len(a)):
    if s == k:
        c.append(i)
    if p == k:
        b.append(i)
    s -= a[i]
    if i < n - 1:
        p += a[i+1]
if (len(b) != 0) and (b[-1] == n-1):
    b = b[:-1]
if (len(c) != 0) and (c[0] == 0):
    c = c[1:]
res = 0
e = len(c)
for i in b:
    res += e - bisect.bisect_left(c, i + 2)
print(res)

