def adds(sin, c):
    if c in sin:
        return 1
    sin.add(c)
    return 0


def corr(v, n):
    if len(v) < n - 1:
        return 0
    sin = {v[0][0], v[0][1]}
    v = v[1:]
    while len(v) > 0:
        nv = []
        for c in v:
            if c[0] in sin:
                if adds(sin, c[1]):
                    return 0
                continue
            if c[1] in sin:
                if adds(sin, c[0]):
                    return 0
                continue
            nv.append(c)
        if v == nv:
            return 0
        v = nv
    if len(sin) == n:
        return 1
    else:
        return 0


n, m = list(map(int, input().split(' ')))
v = []
for c in range(m):
    v.append(list(map(int, input().split(' '))))
if corr(v, n):
    print('yes')
else:
    print('no')
