flag = False


def main():
    intset = []
    qr = int(input())
    for i in range(qr):
        qqss = str(input())
        qqss = qqss.split(" ")
        if qqss[0] == "1":
            a = int(qqss[1])
            b = int(qqss[2])
            intset.append([a, b])
        else:
            si = int(qqss[1])
            fi = int(qqss[2])
            si -= 1
            fi -= 1
            v = [False for x in range(len(intset))]
            printIsPath(intset, si, fi, v)


def printIsPath(iset, a, b, v):
    ast = iset[a][0]
    aen = iset[a][1]
    bst = iset[b][0]
    ben = iset[b][1]
    if bst < ast < ben or bst < aen < ben:
        print("YES")
        return
    v[a] = True
    nonlocal flag
    flag = False
    for i in range(len(iset)):
        mst = iset[i][0]
        men = iset[i][1]
        if (mst < ast < men or mst < aen < men) and not v[i]:
            if searchFinal(iset, i, b, v):
                return
    if not flag:
        print("NO")


def searchFinal(iset, i, f, v):
    v[i] = True
    if i == f:
        print("YES")
        nonlocal flag
        flag = True
        return True
    ist = iset[i][0]
    ien = iset[i][1]
    for j in range(len(iset)):
        jst = iset[j][0]
        jen = iset[j][1]
        if not v[j] and (jst < ist < jen or jst < ien < jen):
            searchFinal(iset, j, f, v)


main()
