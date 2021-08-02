N = int(input())
XY = [tuple(map(int, input().split())) for i in range(N)]
guuki = (XY[0][0] + XY[0][1]) % 2
for x, y in XY:
    if (x + y) % 2 != guuki:
        print(-1)
        return

arms = []
n = 1
for i in range(39):
    arms.append(n)
    n *= 2
if guuki == 0:
    arms.append(1)
arms.reverse()

dirs = {'R': (1, 0), 'U': (0, 1), 'L': (-1, 0), 'D': (0, -1)}

print(len(arms))
print(*arms)
for x, y in XY:
    nx = ny = 0
    s = ''
    if guuki == 0:
        nx += 1
        s += 'R'
    for a in arms[-39:]:
        dist = float('inf')
        dr = ''
        for d, (dx, dy) in dirs.items():
            tmp = abs(x - (nx + dx * a)) + abs(y - (ny + dy * a))
            if tmp < dist:
                dist = tmp
                dr = d
        dx, dy = dirs[dr]
        nx += dx * a
        ny += dy * a
        s += dr
    print(s)
