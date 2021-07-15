#    !/usr/bin/env python3
#    encoding: UTF-8
#    Last Modified: 22/Oct/2019 08:07:05 PM


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


get_array = lambda: list(map(int, sys.stdin.readline().split()))


get_ints = lambda: list(map(int, sys.stdin.readline().split()))


input = lambda: sys.stdin.readline().strip()


def __starting_point():
    main()

__starting_point()
