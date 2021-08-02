import sys


def main():
    x, y = list(map(int, input().split()))
    s = 2 * x + y
    t = 2 * y + x
    if s // 3 - (s % 3 == 0) == t // 3 - (t % 3 == 0):
        print('Brown')
    else:
        print('Alice')


def __starting_point():
    main()


__starting_point()
