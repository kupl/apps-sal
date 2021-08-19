d = {}
n = int(input())
for i in range(n):
    (c, v) = [j for j in input().split()]
    v = ''.join(sorted(v))
    c = int(c)
    if v not in d:
        d[v] = c
    elif d[v] > c:
        d[v] = c
u = [('', 0)] + [(k, v) for (k, v) in list(d.items())]
res = 1000000000
for i1 in range(len(u)):
    for i2 in range(len(u)):
        for i3 in range(len(u)):
            s = u[i1][0] + u[i2][0] + u[i3][0]
            if 'A' in s and 'B' in s and ('C' in s):
                co = u[i1][1] + u[i2][1] + u[i3][1]
                res = min(res, co)
if res == 1000000000:
    print(-1)
else:
    print(res)
