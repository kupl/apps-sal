#!/usr/bin/env python3
# coding: utf-8
# Last Modified: 12/Dec/19 07:08:37 PM


import sys


def main():
    for tc in range(int(input())):
        a, b, c = get_ints()
        A = [a - 1, a, a + 1]
        B = [b - 1, b, b + 1]
        C = [c - 1, c, c + 1]
        ans = 10 ** 18
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    ans = min(
                        ans, abs(A[i] - B[j]) + abs(A[i] - C[k]) + abs(B[j] - C[k])
                    )
        print(ans)


def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return list(map(int, sys.stdin.readline().split()))


def input(): return sys.stdin.readline().strip()


def __starting_point():
    main()


__starting_point()
