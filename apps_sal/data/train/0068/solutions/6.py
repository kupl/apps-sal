gans = []
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, list(input())))
    u = []
    k = 1
    for i in range(1, n):
        if a[i] == a[i - 1]:
            k += 1
        else:
            u.append(k)
            k = 1
    u.append(k)
    dop = 0
    ln = len(u)
    for i in range(ln):
        dop += u[i] - 1
    cur = 0
    ind = 0
    while ind < ln:
        if dop == 0:
            ln -= 1
        else:
            cur += 1
            dop -= 1
        cnt = u[ind] - 1
        if cur < cnt:
            dop -= cnt - cur
            cur = 0
        else:
            cur -= cnt
        ind += 1
    gans.append(ind)
print('\n'.join(map(str, gans)))
