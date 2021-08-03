(n, m) = (int(i) for i in input().split())
tbl = []
for i in range(n):
    crstr = [int(j) for j in input().split()]
    tbl.append(crstr)
true = 0


def prt():
    for xx in range(n):
        for yy in range(m):
            print(tbl[xx][yy], end='	')
        print()
    print()
    print()

# prt()


def lines():
    rows = []
    for i in range(n):
        while 1:
            may = 1
            for j in range(m):
                if tbl[i][j] == 0:
                    for k in range(j):
                        tbl[i][k] += 1
                    may = 0
                    break
                tbl[i][j] -= 1
            if not may:
                break
            rows.append(i + 1)
        # prt()
    return rows


def cols():
    stolbs = []
    for i in range(m):
        while 1:
            may = 1
            for j in range(n):
                if tbl[j][i] == 0:
                    for k in range(j):
                        tbl[k][i] += 1
                    may = 0
                    break
                tbl[j][i] -= 1
            if not may:
                break
            stolbs.append(i + 1)
        # prt()
    return stolbs


if m > n:
    l = lines()
    c = cols()
else:
    c = cols()
    l = lines()

br = 0
for i in range(n):
    for j in range(m):
        if tbl[i][j] != 0:
            br = 1
            break
    if br:
        break
if br:
    print(-1)
else:
    print(len(l) + len(c))
    for i in l:
        print('row', i)
    for i in c:
        print('col', i)
