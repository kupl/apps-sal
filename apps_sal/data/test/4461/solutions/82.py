import sys
h, w = list(map(int, input().split()))
ans = []


def s(a, b):
    for i in range(a):
        s = a * b
        x = i * b
        y = ((a - i) // 2) * b
        z = s - x - y

        d = (a - i) * (b // 2)
        e = s - x - d
        ma = max(x, y, z)
        mi = min(x, y, z)
        mc = max(x, e, d)
        mn = min(x, e, d)
        res = min((ma - mi), (mc - mn))
        ans.append(res)
    return min(ans)


f = s(h, w)
g = s(w, h)
print((min(f, g)))
