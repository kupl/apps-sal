(n, m) = list(map(int, input().split()))
gor = []
ver = []
o = []
for i in range(n):
    gor.append(list(map(int, input().split())))
    o.append([])
for i in range(m):
    ver.append([])
for i in range(m):
    for g in gor:
        ver[i].append(g[i])
ver = list([sorted(list(set(x))) for x in ver])


def f(vg, vr, o):
    vr1 = vr.index(o)
    vg1 = vg.index(o)
    if vr1 > vg1:
        return max([len(vr), len(vg) + vr1 - vg1])
    return max([len(vg), len(vr) + vg1 - vr1])


for (i, vg) in enumerate(gor):
    vg1 = sorted(list(set(vg)))
    for (j, vr) in enumerate(vg):
        o[i].append(f(vg1, ver[j], vr))
for i in o:
    print(' '.join(list(map(str, i))))
