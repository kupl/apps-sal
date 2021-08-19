n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
mp = [[] for i in range(64)]


def getmp(a, b, t):
    return mp[a + b * 4 + t * 16]


for i in range(4):
    for j in range(4):
        mp[(i | j) + (i & j) * 4 + i * 16].append(j)
var = [0]
while len(var) > 0 and len(var) < n:
    vv = var[-1]
    i = len(var) - 1
    p = getmp(a[i], b[i], vv)
    if len(p) == 0:
        appd = True
        while len(var) > 1 and appd:
            vv = var[-1]
            del var[-1]
            i = len(var) - 1
            p = getmp(a[i], b[i], var[-1])
            for t in p:
                if vv < t:
                    p.append(t)
                    appd = False
                    break
        if len(var) == 1:
            if var[0] == 3:
                var = []
            else:
                var[0] += 1
    else:
        var.append(p[0])
if len(var) > 0:
    print('YES')
    print(' '.join(map(str, var)))
else:
    print('NO')
