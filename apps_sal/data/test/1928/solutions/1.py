def getCells(n, m, k):
    penalty = 0
    cells = []
    for l in range(2, n + m + 1):
        iLeft = 1 if l - 1 <= m else l - m
        iRight = n if l - n > 0 else l - 1
        for i in range(iLeft, iRight + 1):
            j = l - i
            penalty += l - 1
            cells.append((i, j))
            k -= 1
            if k == 0:
                return penalty, cells


def getPath(i, j):
    path = []
    p, q = 1, 1
    while p < i:
        path.append((p, q))
        p += 1
    while q < j:
        path.append((p, q))
        q += 1
    path.append((i, j))
    return path


n, m, k = map(int, input().split())
penalty, cells = getCells(n, m, k)
print(penalty)
for cell in reversed(cells):
    print(*getPath(*cell))
