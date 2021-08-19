def get_neighbors(i, j):
    neighbors = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x != y:
                if x == 0 or y == 0:
                    if x + i >= 0 and y + j >= 0 and (x + i <= 2) and (y + j <= 2):
                        neighbors.append((x + i, y + j))
    return neighbors


def lights_out(lst):
    res = [x[:] for x in lst]
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            for (x, y) in get_neighbors(i, j):
                res[i][j] += lst[x][y]
    return res


def __starting_point():
    lst = [0, 0, 0]
    for i in range(3):
        lst[i] = [int(x) for x in input().split()]
    res = lights_out(lst)
    for line in res:
        for entry in line:
            print((entry + 1) % 2, end='')
        print()


__starting_point()
