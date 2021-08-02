n, m = list(map(int, input().split()))
pole = []
unfitted = []


def star_fits(x, y, r):

    if x - r >= 0 and x + r < m and y - r >= 0 and y + r < n:
        res = True
        for k in range(x - r, x + r + 1):
            if pole[y][k] != '*':
                res = False
        for k in range(y - r, y + r + 1):
            if pole[k][x] != '*':
                res = False
    else:
        return False
    return res


def get_max_r(x, y):
    r = 1
    while (x - r >= 0) and (x + r < m) and (y - r >= 0) and (y + r < n):
        if pole[y][x + r] == '*' and pole[y][x - r] == '*' and pole[y + r][x] == '*' and pole[y - r][x] == '*':
            r += 1
        else:
            return r - 1
    return r - 1


def mark_star(x, y, r):
    if x - r >= 0 and x + r < m and y - r >= 0 and y + r < n:
        for k in range(x - r, x + r + 1):
            unfitted[y][k] = False
        for k in range(y - r, y + r + 1):
            unfitted[k][x] = False


for i in range(n):
    pole.append(input().strip()[:m])
    unfitted.append([True] * m)

fin_res = []
for x in range(m):
    for y in range(n):
        if pole[y][x] == '*':
            r = get_max_r(x, y)
            if r > 0:
                mark_star(x, y, r)
                # print('found atar at', x,y,r)
                fin_res.append((y + 1, x + 1, r))


for x in range(m):
    for y in range(n):
        if pole[y][x] == '*' and unfitted[y][x]:
            print(-1)
            return

print(len(fin_res))
for t in fin_res:
    print(*t)
