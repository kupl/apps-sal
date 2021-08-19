def fun(n, q, c, stars, querry):
    m = 100
    precom = [[[0] * m for _ in range(m)] for _ in range(c + 1)]
    for (x, y, p) in stars:
        for i in range(c + 1):
            temp = (p + i) % (c + 1)
            precom[i][x - 1][y - 1] += temp
    for k in range(c + 1):
        for i in range(0, m):
            for j in range(1, m):
                precom[k][i][j] += precom[k][i][j - 1]
    for k in range(c + 1):
        for j in range(0, m):
            for i in range(1, m):
                precom[k][i][j] += precom[k][i - 1][j]
    for (t, x1, y1, x2, y2) in querry:
        t = t % (c + 1)
        (x1, y1, x2, y2, a, b, C, d) = (x1 - 1, y1 - 1, x2 - 1, y2 - 1, 0, 0, 0, 0)
        a = precom[t][x2][y2]
        if x1 != 0:
            b = precom[t][x1 - 1][y2]
        if y1 != 0:
            C = precom[t][x2][y1 - 1]
        if x1 != 0 and y1 != 0:
            d = precom[t][x1 - 1][y1 - 1]
        print(a - b - C + d)


(n, q, c) = list(map(lambda x: int(x), input().split()))
stars = [list(map(lambda x: int(x), input().split())) for _ in range(n)]
querry = [list(map(lambda x: int(x), input().split())) for _ in range(q)]
fun(n, q, c, stars, querry)
