(h, w) = map(int, input().split())
s = []
for i in range(h):
    li = input()
    s.append(li)


def check(s, x, y, w, h):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        (ny, nx) = (y + dy[i], x + dx[i])
        if 0 <= nx < w and 0 <= ny < h:
            if s[ny][nx] == '#':
                return True
    return False


ok = True
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            ok = check(s, j, i, w, h)
            if not ok:
                break
    if not ok:
        break
if ok or (w == 1 and h == 1):
    print('Yes')
else:
    print('No')
