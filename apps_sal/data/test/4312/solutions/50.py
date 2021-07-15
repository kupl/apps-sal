# coding=utf-8
import sys

def __starting_point():
    A, B, C, D = list(map(int, input().split()))

    while True:
        C -= B
        if C <= 0:
            print('Yes')
            return

        A -= D
        if A <= 0:
            print('No')
            return

__starting_point()
