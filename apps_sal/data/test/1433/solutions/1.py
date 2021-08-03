def f():
    n, m = list(map(int, input().split()))
    S = [list(map(int, input().split())) for i in range(n)]

    strp = [[S[i][0]] for i in range(n)]
    for i in range(n):
        for j in range(1, m):
            strp[i].append(strp[i][j - 1] + S[i][j])
    stbp = [[S[0][j]] for j in range(m)]
    for j in range(m):
        for i in range(1, n):
            stbp[j].append(stbp[j][i - 1] + S[i][j])

    def good(x, y, d):
        if S[x][y] == 1:
            return False
        else:
            d = 'ruld'.find(d)
            if not d % 2:
                return bool(strp[x][y] if d == 0 else strp[x][-1] - strp[x][y])
            else:
                return bool(stbp[y][x] if d == 1 else stbp[y][-1] - stbp[y][x])

    cnt = 0
    for x in range(n):
        for y in range(m):
            cnt += good(x, y, 'r') + \
                good(x, y, 'u') + \
                good(x, y, 'l') + \
                good(x, y, 'd')

    print(cnt)


f()
