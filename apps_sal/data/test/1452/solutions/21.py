mod = 1000000007
res = 1
h, w = list(map(lambda x: int(x), input().split()))
pole = [[0 for x in range(w)] for y in range(h)]
rs = list(map(lambda x: int(x), input().split()))
ls = list(map(lambda x: int(x), input().split()))
for i in range(h):
    for x in range(rs[i]):
        pole[i][x] = 1
    if rs[i] != w:
        pole[i][rs[i]] = -1
# print(pole)
for i in range(w):
    for y in range(ls[i]):
        if pole[y][i] == -1:
            print(0)
            return
        else:
            pole[y][i] = 1
    if ls[i] != h:
        if pole[ls[i]][i] == 1:
            print(0)
            return
        pole[ls[i]][i] = -1
for y in pole:
    for x in y:
        if x == 0:
            res <<= 1
            res = res % mod
print(res)
