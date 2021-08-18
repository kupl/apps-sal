n, c = list(map(int, input().split()))
a = list(map(int, input().split()))


nc = 0
last = {}
preconfs = []
preconfc = []
for i in range(n):
    if a[i] == c:
        nc += 1
        last[c] = i
        preconfs.append(i)
    else:
        if not (a[i] in last):
            preconfs.append(1)
        else:
            preconfs.append(preconfs[last[a[i]]] + 1)
        last[a[i]] = i
    preconfc.append(nc)


content = {}
for i in range(n):
    if a[i] in content:
        content[a[i]][0] += 1
        content[a[i]].append(i)
    else:
        content[a[i]] = [1, i]


def val(i, j):
    if a[i] == a[j]:
        return nc + (preconfs[j] - preconfs[i] + 1) - (preconfc[j] - preconfc[i]) + (a[i] == c and -1 or 0)
    print("erreur")


def rec_sol(i, j, tab):
    if (i == j):
        return (i, i, j, j)

    k = (i + j) // 2
    r1 = rec_sol(i, k, tab)
    r2 = rec_sol(k + 1, j, tab)

    i1 = max([r1[0], r2[0]], key=lambda x: val(tab[x], tab[j]))
    i2, i3 = max([(r1[0], r2[3]), (r1[1], r1[2]), (r2[1], r2[2]), (r1[0], j)], key=lambda x: val(tab[x[0]], tab[x[1]]))
    i4 = max([r1[3], r2[3]], key=lambda x: val(tab[i], tab[x]))
    return (i1, i2, i3, i4)


def get_sol(k):
    s = rec_sol(1, content[k][0], content[k])
    return val(content[k][s[1]], content[k][s[2]])


res = []
for i in content:
    if (i != c):
        res.append(get_sol(i))
if res:
    print(max(res))
else:
    print(n)
