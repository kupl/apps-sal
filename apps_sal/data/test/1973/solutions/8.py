def ii():
    return int(input())


def kk():
    return list(map(int, input().split()))


def k2():
    return [int(x) - 1 for x in input().split()]


def ll():
    return list(kk())


n = ii()
d = [0] * 10
maxi = 2
for (j, v) in enumerate(k2()):
    d[v] += 1
    vs = {}
    for i in range(10):
        if d[i] == 0:
            continue
        if d[i] not in vs:
            vs[d[i]] = 0
        vs[d[i]] += 1
    if len(vs) > 2:
        continue
    if len(vs) == 2:
        val = max(list(vs.keys()))
        if 1 in vs and vs[1] == 1 or (val - 1 in vs and vs[val] == 1):
            maxi = j
    elif len(vs) == 1 and (1 in vs or d.count(0) == 9):
        maxi = j
print(max(maxi + 1, min(2, n)))
