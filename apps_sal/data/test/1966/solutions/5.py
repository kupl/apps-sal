n = int(input())
p = [[[] for _ in range(n)] for _ in range(4)]
for i in range(4):
    for j in range(n):
        r = list(map(int, list(input())))
        p[i][j] = r
    if i < 3:
        input()
dif = [0] * 4
for k in range(4):
    o = 0
    for i in range(n):
        for j in range(n):
            if p[k][i][j] == (n * i + j) % 2:
                o += 1
    dif[k] = (o, n * n - o)
res = 10 ** 19
z = sum((dif[_][1] for _ in range(4)))
for k1 in range(4):
    for k2 in range(k1 + 1, 4):
        res = min(res, dif[k1][0] + dif[k2][0] + z - dif[k1][1] - dif[k2][1])
print(res)
