n = int(input())
tbl = []
for i in range(n):
    tbl.append(list(map(int, input().split())))

out = False
for i, row in enumerate(tbl):
    for j in range(len(row)):
        out = False
        e = row[j]
        if e == 1:
            out = True
            continue
        for j1, e1 in enumerate(row):
            if j1 != j:
                for i1 in range(n):
                    if e1 + tbl[i1][j] == e:
                        out = True
                        break
            if out:
                break
        if not out:
            print('No')
            break
    if not out:
        break
if out:
    print('Yes')
