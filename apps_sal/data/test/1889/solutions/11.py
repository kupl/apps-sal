values = []


def get_max(row):
    total = 0
    max_vv = 0

    for x in row:
        if x == 1:
            max_vv += 1
        else:
            if max_vv > total:
                total = max_vv
            max_vv = 0

    if max_vv > total:
        total = max_vv

    return total


def __starting_point():
    n, m, q = map(int, input().split())
    rows = []

    for i in range(n):
        rows.append(list(map(int, input().split())))
        values.append(get_max(rows[-1]))

    for i in range(q):
        i, j = map(int, input().split())
        i -= 1
        j -= 1

        rows[i][j] = 1 - rows[i][j]
        values[i] = get_max(rows[i])

        print(max(values))
__starting_point()
