def solve():
    (n, m) = map(int, input().split())
    tab = [list(map(int, input().split())) for _ in range(n)]

    def ordered(l):
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                return False
        return True

    def canswap(l):
        if ordered(l):
            return True
        for i in range(len(l)):
            for j in range(i + 1, len(l)):
                lc = list(l)
                (lc[i], lc[j]) = (lc[j], lc[i])
                if ordered(lc):
                    return True
        return False
    works = True
    for row in tab:
        if not canswap(row):
            works = False
    if works:
        return True
    for coli in range(m):
        for colj in range(coli, m):
            works = True
            for rowref in tab:
                row = list(rowref)
                (row[coli], row[colj]) = (row[colj], row[coli])
                if ordered(row):
                    continue
                good = False
                for i in range(m):
                    if good:
                        break
                    for j in range(m):
                        row = list(rowref)
                        (row[i], row[j]) = (row[j], row[i])
                        (row[coli], row[colj]) = (row[colj], row[coli])
                        if ordered(row):
                            good = True
                            break
                        row = list(rowref)
                        (row[coli], row[colj]) = (row[colj], row[coli])
                        (row[i], row[j]) = (row[j], row[i])
                        if ordered(row):
                            good = True
                            break
                if not good:
                    works = False
                    break
            if works:
                return True
    return False


res = solve()
print('YES' if res else 'NO')
