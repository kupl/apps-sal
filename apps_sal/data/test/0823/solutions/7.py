x, y = list(map(int, input().split()))
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]


def onl(x1, y1, x2, y2):
    if x1 == x2:
        return x == x1 and y in range(min(y1, y2), max(y1, y2) + 1)
    elif y1 == y2:
        return y == y1 and x in range(min(x1, x2), max(x1, x2) + 1)


def sp(cx, cy, t):
    l = t // 2 + 1
    nx, ny = cx + dx[t % 4] * l, cy + dy[t % 4] * l
    return t if onl(cx, cy, nx, ny) else sp(nx, ny, t + 1)


print(sp(0, 0, 0))
