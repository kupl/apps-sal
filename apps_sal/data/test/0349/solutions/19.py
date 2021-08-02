def main():
    n, m = list(map(int, input().split()))
    m1 = [[] for _ in range(n)]
    m2 = [[] for _ in range(n)]
    for i in range(n):
        m1[i] = list(map(int, input().split()))
    for i in range(n):
        m2[i] = list(map(int, input().split()))

    for r in range(n):
        for c in range(m):
            m1[r][c], m2[r][c] = min(m1[r][c], m2[r][c]), max(m1[r][c], m2[r][c])

    def checkRow(row):
        for i in range(m - 1):
            if m1[row][i] >= m1[row][i + 1] or m2[row][i] >= m2[row][i + 1]:
                return False
        return True

    def checkCol(col):
        for i in range(n - 1):
            if m1[i][col] >= m1[i + 1][col] or m2[i][col] >= m2[i + 1][col]:
                return False
        return True

    ok = True
    for r in range(n):
        if not checkRow(r):
            ok = False
            break

    if ok:
        for c in range(m):
            if not checkCol(c):
                ok = False
                break

    print('Possible' if ok else 'Impossible')


def __starting_point():
    main()


__starting_point()
