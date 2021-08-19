n = int(input())
minx = miny = maxx = maxy = 0
c = []
dx = {}
dy = {}
for i in range(4 * n + 1):
    (x, y) = list(map(int, input().split(' ')))
    c.append([x, y])
    if x not in dx:
        dx[x] = 1
    else:
        dx[x] += 1
    if y not in dy:
        dy[y] = 1
    else:
        dy[y] += 1
minx = miny = maxx = maxy = 0
for i in sorted(dx.keys()):
    if dx[i] >= 2 and minx == 0:
        minx = i
        break
for i in sorted(dy.keys()):
    if dy[i] >= 2 and miny == 0:
        miny = i
        break
for i in list(reversed(sorted(dx.keys()))):
    if dx[i] >= 2 and maxx == 0:
        maxx = i
        break
for i in list(reversed(sorted(dy.keys()))):
    if dy[i] >= 2 and maxy == 0:
        maxy = i
        break
for i in c:
    if minx <= i[0] <= maxx and miny <= i[1] <= maxy:
        if (i[0] != minx and i[0] != maxx) and (i[1] != miny and i[1] != maxy):
            print(i[0], i[1])
            break
    else:
        print(i[0], i[1])
        break
