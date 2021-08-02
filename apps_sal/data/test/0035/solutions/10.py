def satisfy_line(line):
    total = len(line)
    size = total // 3
    if total % 3 != 0:
        return False

    first_part = line[0:size]
    second_part = line[size:2 * size]
    third_part = line[2 * size:3 * size]

    first_set = set(first_part)
    second_set = set(second_part)
    third_set = set(third_part)

    if len(first_set) == len(second_set) == len(third_set) == 1:
        all_color = set().union(first_set, second_set, third_set)
        if all_color == {'R', 'G', 'B'}:
            return True
    return False


def satisfy_flag(flag):
    first_line = flag[0]

    if not satisfy_line(first_line):
        return False

    for line in flag:
        if line != first_line:
            return False

    return True


def rotate(flag, n, m):
    rotated_flag = []

    for i in range(m):
        line = []
        for j in range(n):
            line.append(flag[j][i])
        rotated_flag.append(line)

    return rotated_flag


def main():
    n, m = [int(t) for t in input().split()]
    flag = [input() for _ in range(n)]

    if satisfy_flag(flag):
        print('YES')
    elif satisfy_flag(rotate(flag, n, m)):
        print('YES')
    else:
        print('NO')


def __starting_point():
    main()


__starting_point()
