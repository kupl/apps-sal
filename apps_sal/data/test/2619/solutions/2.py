(n, q, c) = list(map(int, input().split()))
stars = [list(map(int, input().split())) for i in range(n)]
queries = [list(map(int, input().split())) for i in range(q)]
prec = [[[0 for y in range(101)] for x in range(101)] for i in range(c + 1)]
for (x, y, s) in stars:
    for t in range(c + 1):
        prec[t][x][y] += s + t if s + t <= c else s + t - (c + 1)
for s in range(len(prec)):
    for x in range(len(prec[s])):
        for y in range(len(prec[s][x])):
            if x and y:
                prec[s][x][y] += prec[s][x - 1][y] + prec[s][x][y - 1] - prec[s][x - 1][y - 1]
for (t, x1, y1, x2, y2) in queries:
    s = t % (c + 1)
    res = prec[s][x2][y2] - prec[s][x1 - 1][y2] - prec[s][x2][y1 - 1] + prec[s][x1 - 1][y1 - 1]
    print(res)
