nmk = input()
(ns, ms, ks) = nmk.split(' ')
n = int(ns)
m = int(ms)
k = int(ks)
counter = 1
field = [[[0, 0] for i in range(m)] for j in range(n)]
res = 0
while counter <= k:
    xy = input()
    (xs, ys) = xy.split(' ')
    x = int(xs) - 1
    y = int(ys) - 1
    if field[x][y][0] == 0:
        field[x][y][1] = counter
    field[x][y][0] = 1
    counter += 1
for i in range(n - 1):
    for j in range(m - 1):
        sum = field[i + 1][j][0] + field[i][j + 1][0] + field[i + 1][j + 1][0] + field[i][j][0]
        if sum == 4:
            a = max(field[i + 1][j][1], field[i][j + 1][1], field[i + 1][j + 1][1], field[i][j][1])
            if res == 0:
                res = a
            elif a < res:
                res = a
print(res)
