from bisect import bisect
t = input
p = print
r = range
n = int(t())
x = list(map(int, t().split()))
q = int(t())
a = [0] * q
for i in r(q):
    a[i] = int(t())
x.sort()
for i in a:
    index = bisect(x, i)
    p(index)
