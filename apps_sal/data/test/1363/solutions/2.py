def sub_pairs(r, l):
    if r - l < 2:
        return 0
    n = r - l
    return (n * (n - 1)) // 2


def sub_triples(r, l):
    if r - l < 3:
        return 0
    n = r - l
    return (n * (n - 1) * (n - 2)) // 6


def fast(g, d, f):
    g.sort()
    d.sort()
    f.sort()
    res = 0
    gl, dl, fl = 0, 0, 0
    gr, dr, fr = 0, 0, 0
    while gl < len(g) and dl < len(d) - 1 and fl < len(f) - 2:
        mn = min(g[gl], d[dl], f[fl])
        mx = mn * 2
        while gr < len(g) and g[gr] <= mx:
            gr += 1
        while dr < len(d) and d[dr] <= mx:
            dr += 1
        while fr < len(f) and f[fr] <= mx:
            fr += 1
        if g[gl] == mn:
            res += sub_pairs(dr, dl) * sub_triples(fr, fl)
            gl += 1
        elif d[dl] == mn:
            res += (max(0, dr - dl - 1)) * max(0, gr - gl) * sub_triples(fr, fl)
            dl += 1
        else:
            res += sub_pairs(fr, fl + 1) * max(0, gr - gl) * sub_pairs(dr, dl)
            fl += 1
    return res


input()
g = [int(x) for x in input().split()]
d = [int(x) for x in input().split()]
f = [int(x) for x in input().split()]
print(fast(g, d, f))
