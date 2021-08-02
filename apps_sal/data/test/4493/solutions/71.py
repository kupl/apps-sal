c = [list(map(int, input().split())) for _ in range(3)]

ok = True

lis = [[0, 1], [1, 2], [2, 0]]

d = [[c[l[0]][i] - c[l[1]][i] for i in range(3)]for l in lis]
e = [[c[i][l[0]] - c[i][l[1]] for i in range(3)]for l in lis]

for i in range(3):
    if d[i].count(d[i][0]) != 3:
        ok = False
    if e[i].count(e[i][0]) != 3:
        ok = False

if ok:
    print('Yes')
else:
    print('No')
