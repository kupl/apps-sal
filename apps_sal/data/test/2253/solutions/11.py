import sys


def main():
    for tc in range(int(input())):
        s = list(input())
        s.reverse()
        if s[0] == 'o':
            print('FILIPINO')
        elif s[0] == 'u':
            print('JAPANESE')
        else:
            print('KOREAN')


def get_array():
    return list(map(int, sys.stdin.readline().split()))


def get_ints():
    return list(map(int, sys.stdin.readline().split()))


def input():
    return sys.stdin.readline().strip()


def __starting_point():
    main()


__starting_point()
