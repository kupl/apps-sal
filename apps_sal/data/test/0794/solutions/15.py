import sys


def get_array():
    return list(map(int, sys.stdin.readline().split()))


def get_ints():
    return list(map(int, sys.stdin.readline().split()))


def input():
    return sys.stdin.readline().strip()


def main():
    n = int(input())
    arr = get_array()
    arr.sort()
    if sum(arr[:n]) != sum(arr[n:]):
        print(*arr)
    else:
        print(-1)


def __starting_point():
    main()


__starting_point()
