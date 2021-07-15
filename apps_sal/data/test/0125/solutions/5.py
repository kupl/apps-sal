arr = [list() for i in range(4)]
arrp = []
for i in range(4):
    l, s, r, p = [int(i) for i in input().split()]
    arr[i].extend([l, s, r])
    arr[[3, i - 1][i > 0]].append(l)
    arr[[0, i + 1][i < 3]].append(r)
    arr[(i + 2) % 4].append(s)
    arrp.append(p)
for i in range(4):
    if arrp[i]:
        if 1 in arr[i]:
            print('YES')
            break
else:
    print('NO')

