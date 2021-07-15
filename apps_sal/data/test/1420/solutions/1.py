__author__ = 'PrimuS'

n, l = (int(x) for x in input().split())
a = [int(x) for x in input().split()]
a.sort()
k = len(a)
d = max(a[0], l - a[len(a) - 1])
for i in range(k - 1):
    dd = (a[i+1] - a[i]) / 2
    d = max(d, dd)

print(d)
