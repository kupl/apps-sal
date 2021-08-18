
from sys import stdin


def main():
    n, m = stdin_get_ints_from_line()

    colored = ['C', 'M', 'Y']

    for i in range(n):
        pixels = stdin_get_string_from_line().split(' ')
        for pixel in pixels:
            if pixel in colored:
                print('
                return
    print('

    return


def stdin_get_ints_from_line():
    return (int(x) for x in stdin.readline().strip().split(' '))


def stdin_get_ints_list_from_line():
    return list(int(x) for x in stdin.readline().strip().split(' '))


def stdin_get_string_from_line():
    return stdin.readline().strip()


def __starting_point():
    main()


__starting_point()
