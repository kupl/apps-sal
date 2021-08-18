n, ma, mb = list(map(int, input().split()))
el = [list(map(int, input().split())) for i in range(n)]
sa = sum(i[0] for i in el)
sb = sum(i[1] for i in el)
inf = 10000000000
x = [[inf for j in range(sb + 1)] for i in range(sa + 1)]
x[0][0] = 0
for i in range(n):
    now = el[i]
    x_sub = [[0 for j in range(sb + 1)] for i in range(sa + 1)]
    for k in range(sa + 1):
        for l in range(sb + 1):
            if x[k][l] != inf and k + now[0] < sa + 1 and l + now[1] < sb + 1:
                x_sub[k + now[0]][l + now[1]] = x[k][l] + now[2]
    for k in range(sa + 1):
        for l in range(sb + 1):
            if x_sub[k][l] != 0:
                x[k][l] = min(x[k][l], x_sub[k][l])
mi = min(sa // ma, sb // mb)
ans = inf
for i in range(1, mi + 1):
    ans = min(ans, x[ma * i][mb * i])
if ans == inf:
    print((-1))
else:
    print(ans)
