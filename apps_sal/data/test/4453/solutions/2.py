#    !/usr/bin/env python3
#    encoding: UTF-8
#    Last Modified: 22/Oct/2019 08:13:15 PM


import sys


def main():
    for tc in range(int(input())):
        n = int(input())
        arr = get_array()
        ans = [1] * n
        for i in range(n):
            j = arr[i] - 1
            while j != i:
                ans[i] += 1
                j = arr[j] - 1
        print(*ans)


get_array = lambda: list(map(int, sys.stdin.readline().split()))


get_ints = lambda: list(map(int, sys.stdin.readline().split()))


input = lambda: sys.stdin.readline().strip()


def __starting_point():
    main()


__starting_point()
