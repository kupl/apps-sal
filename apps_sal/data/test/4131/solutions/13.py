import bisect
n, m = map(int, input().split())
x = [list() for i in range(n)]
p = []
y = []
for i in range(m):
    s, t = map(int, input().split())
    p.append(s)
    y.append(t)
    x[s - 1].append(t)
for i in range(n):
    x[i].sort()

for i in range(m):
    index = bisect.bisect_left(x[p[i] - 1], y[i])
    print("{:06}{:06}".format(p[i], index + 1))
