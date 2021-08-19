#!/usr/bin/env python3
# coding: utf-8
# Last Modified: 22/Jan/20 08:07:33 PM


import sys


def main():
    for tc in range(int(input())):
        a, b, c, n = get_ints()
        x = a + b + c + n
        if x % 3 != 0:
            print("NO")
        else:
            y = max(a, b, c)
            if (x // 3) >= y:
                print("YES")
            else:
                print("NO")


def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return list(map(int, sys.stdin.readline().split()))


def input(): return sys.stdin.readline().strip()


def __starting_point():
    main()


__starting_point()
