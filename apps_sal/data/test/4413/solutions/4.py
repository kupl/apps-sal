import sys


def main():
    for tc in range(int(input())):
        n = int(input())
        arr = get_array()
        arr.sort()
        f = 0
        for i in range(1, n):
            if arr[i] == 1 + arr[i - 1]:
                f = 1
        if f == 1:
            print(2)
        else:
            print(1)


def get_array():
    return list(map(int, sys.stdin.readline().split()))


def get_ints():
    return list(map(int, sys.stdin.readline().split()))


def input():
    return sys.stdin.readline().strip()


def __starting_point():
    main()


__starting_point()
