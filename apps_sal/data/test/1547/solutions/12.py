n, m, k = [int(i) for i in input().split()]

printops = []
for i in range(k):
    printops.append([int(i) for i in input().split()])


def pm():
    for r in matrix:
        for i in r:
            print(i, end=' ')
        print()


row_status = [True] * n
col_status = [True] * m

matrix = [[0] * m for i in range(n)]
for i in range(k):
    j = k - i - 1
    rc_indicator, rc, color = printops[j]
    rc -= 1

    if rc_indicator == 1:
        if row_status[rc]:
            for c in range(m):
                if col_status[c]:
                    matrix[rc][c] = color
            row_status[rc] = False
    else:
        if col_status[rc]:
            for r in range(n):
                if row_status[r]:
                    matrix[r][rc] = color
            col_status[rc] = False

pm()
