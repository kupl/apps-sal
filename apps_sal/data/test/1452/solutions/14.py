h, w = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
tab = [[0] * w for i in range(h)]
arr = 0
for i in range(h):
    if a[i] == 0:
        tab[i][0] = 2
    else:
        for j in range(a[i]):
            tab[i][j] = 1
        if a[i] < w:
            tab[i][a[i]] = 2
for i in range(w):
    if b[i] == 0:
        if tab[0][i] == 1:
            print(0)
            return
        tab[0][i] = 2
    else:
        for j in range(b[i]):
            if tab[j][i] == 2:
                print(0)
                return
            tab[j][i] = 1
        if b[i] < h:
            if tab[b[i]][i] == 1:
                print(0)
                return
            tab[b[i]][i] = 2
for i in range(h):
    for j in range(w):
        if tab[i][j] == 0:
            arr += 1
print(pow(2, arr, (10**9 + 7)))
