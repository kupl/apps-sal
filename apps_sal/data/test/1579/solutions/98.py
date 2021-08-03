import sys
sys.setrecursionlimit(100000)

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
xtoy = {}
ytox = {}
for x, y in xy:
    if x not in xtoy:
        xtoy[x] = [y]
    else:
        xtoy[x].append(y)
    if y not in ytox:
        ytox[y] = [x]
    else:
        ytox[y].append(x)


def doit(x, xs, ys, xtoy, ytox):
    ret = 0
    if x in xtoy:
        xs.add(x)
        yl = xtoy.pop(x)
        ret += len(yl)
        for y in yl:
            ret += doit(y, ys, xs, ytox, xtoy)
    return ret


ret = 0
while len(xtoy) > 0:
    x = next(iter(xtoy))
    xs = set()
    ys = set()
    num = doit(x, xs, ys, xtoy, ytox)
    ret += len(xs) * len(ys) - num // 2

print(ret)
