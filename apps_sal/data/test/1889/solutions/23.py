def read_data():
    n, m, q = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append(list(map(int, input().split())))
    qs = []
    for i in range(q):
        x, y = map(int, input().split())
        qs.append((x - 1, y - 1))
    return n, m, q, grid, qs


def max_cons(row):
    mc = 0
    tmp = 0
    for v in row:
        if v:
            tmp += 1
        else:
            if tmp > mc:
                mc = tmp
            tmp = 0
    return max(mc, tmp)


def solve(n, m, q, grid, qs):
    mcc = [max_cons(row) for row in grid]
    for x, y in qs:
        row = grid[x]
        row[y] = 1 - row[y]
        mcc[x] = max_cons(row)
        print(max(mcc))


param = read_data()
solve(*param)
