def read_ints():
    return [int(x) for x in input(' ').split()]


def main():
    (n, m) = read_ints()
    field = []
    (x, y) = (None, None)
    for i in range(n):
        line = input()
        if 'S' in line:
            (x, y) = (i, line.find('S'))
        field.append(list(line))
    field[x][y] = '*'
    flag = False
    (curr_x, curr_y) = (x, y)
    delta = [(-1, 0, 'U'), (+1, 0, 'D'), (0, -1, 'L'), (0, +1, 'R')]
    (par_x, par_y) = (-1, -1)
    while True:
        if flag:
            field[curr_x][curr_y] = 'U'
        flag = True
        for (dx, dy, label) in delta:
            (next_x, next_y) = (curr_x + dx, curr_y + dy)
            if not 0 <= next_x < n:
                continue
            if not 0 <= next_y < m:
                continue
            if par_x == next_x and par_y == next_y:
                continue
            if field[next_x][next_y] == '*':
                print(label, end='', flush=True)
                (par_x, par_y) = (curr_x, curr_y)
                (curr_x, curr_y) = (next_x, next_y)
                break
        if x == curr_x and y == curr_y:
            break


def __starting_point():
    main()


__starting_point()
