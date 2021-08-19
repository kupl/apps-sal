import bisect
(s, b) = map(int, input().split())
a = list(map(int, input().split()))
d = []
for i in range(b):
    d.append(list(map(int, input().split())))
d = sorted(d)
c = []
p = []
for i in range(len(d)):
    c.append(d[i][0])
    p.append(d[i][1])
k = [p[0]]
for i in range(1, len(p)):
    k.append(k[-1] + p[i])
for i in range(len(a)):
    l = bisect.bisect_right(c, a[i])
    if l == 0:
        print(0, end=' ')
    else:
        print(k[l - 1], end=' ')
