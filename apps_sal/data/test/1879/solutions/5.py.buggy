t, sx, sy, ex, ey = tuple(map(int, input().split()))
dx, dy = ex - sx, ey - sy
op = {'W': 0, 'E': 0, 'S': 0, 'N': 0}
if dx < 0:
    op['W'] = -dx
if dx > 0:
    op['E'] = dx
if dy < 0:
    op['S'] = -dy
if dy > 0:
    op['N'] = dy
if (dx, dy) == (0, 0):
    print(0)
    return
now = 0
for wind in input():
    if op[wind] > 0:
        op[wind] -= 1
    now += 1
    if sum(op.values()) == 0:
        print(now)
        break
else:
    print(-1)
