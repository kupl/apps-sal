#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import sys
import bisect
from collections import Counter


def read_int(): return int(sys.stdin.readline())


def read_ints(): return list(map(int, sys.stdin.readline().split()))
def read_int_list(): return list(read_ints())
def read(): return sys.stdin.readline().strip()
def read_list(): return sys.stdin.readline().split()


def main():
    n = read_int()
    a = read_int_list()
    b = read_int_list()
    sa, sb = 0, 0
    a.sort()
    b.sort()
    turn = True
    while a or b:
        if turn:
            if a:
                if b:
                    if a[-1] > b[-1]:
                        sa += a.pop()
                    else:
                        b.pop()
                else:
                    sa += a.pop()
            else:
                b.pop()
        else:
            if b:
                if a:
                    if b[-1] > a[-1]:
                        sb += b.pop()
                    else:
                        a.pop()
                else:
                    sb += b.pop()
            else:
                a.pop()
        turn = not turn
    print(sa - sb)


main()
