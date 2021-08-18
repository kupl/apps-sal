
from sys import stdin


def main():
    r, c = stdin_get_ints_from_line()

    a = []

    for _ in range(r):
        a.append(stdin_get_ints_list_from_line())

    good = 0

    col_have = [0] * 1000
    row_have = [0] * 1000

    zeros_left = [0] * 1000
    zeros_up = [0] * 1000

    for row in range(r):
        for col in range(c):
            if a[row][col] == 1:
                row_have[row] = 1
                col_have[col] = 1

                good += zeros_left[row]
                zeros_left[row] = 0

                good += zeros_up[col]
                zeros_up[col] = 0
                continue

            zeros_left[row] += 1
            zeros_up[col] += 1
            if row_have[row] == 1:
                good += 1
            if col_have[col] == 1:
                good += 1

    print(good)


def stdin_get_ints_from_line():
    return (int(x) for x in stdin.readline().strip().split(' '))


def stdin_get_ints_list_from_line():
    return list(int(x) for x in stdin.readline().strip().split(' '))


def stdin_get_string_from_line():
    return stdin.readline().strip()


def __starting_point():
    main()


__starting_point()
