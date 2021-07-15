def _win(a, b, c, d):
    if a[0] > c[1] and b[1] > d[0]:
        return 1
    elif a[0] < c[1] and b[1] < d[0]:
        return -1
    else:
        return 0


def win(a, b, c, d):
    nonlocal p
    return _win(p[a], p[b], p[c], p[d])


def win_comb(a, b, c, d):
    x, y = win(a, b, c, d), win(a, b, d, c)
    if x == 1 and y == 1:
        return 1
    if x == -1 or y == -1:
        return -1
    return 0


def win_team1(a, b, c, d):
    x, y = win_comb(a, b, c, d), win_comb(b, a, c, d)
    if x == 1 or y == 1:
        return 1
    if x == -1 and y == -1:
        return -1
    return 0

p = []
for i in range(4):
    p.append(tuple(map(int, input().split())))
w = win_team1(0, 1, 2, 3)
if w == 1:
    print('Team 1')
elif w == -1:
    print('Team 2')
else:
    print('Draw')

