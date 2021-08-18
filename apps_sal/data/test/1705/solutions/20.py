

import sys

inf = float("inf")
mod = 1000000007


def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return list(map(int, sys.stdin.readline().split()))


def input(): return sys.stdin.readline()


def main():
    n = int(input())
    arr = get_array()
    x = arr[-1]
    for i in range(n):
        if arr[i] != x:
            index = i
    print(index + 1)


def __starting_point():
    main()


__starting_point()
