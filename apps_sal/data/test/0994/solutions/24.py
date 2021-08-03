from sys import stdin
input = stdin.readline

n, m = (int(x) for x in input().split())
pd, ph = (int(x) for x in input().split())
res = ph + pd - 1
for i in range(1, m):
    d, h = (int(x) for x in input().split())
    dd = d - pd
    dh = abs(h - ph)
    if dd < dh:
        print('IMPOSSIBLE')
        return
    dd -= dh
    res = max(res, max(ph, h) + dd // 2)
    pd = d
    ph = h
res = max(res, ph + (n - pd))
print(res)
