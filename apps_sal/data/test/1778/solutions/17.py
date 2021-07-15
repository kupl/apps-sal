#!/usr/bin/env python3
#-*- encoding: utf-8 -*-

import sys
import bisect
from collections import Counter

read_int = lambda : int(sys.stdin.readline())
read_ints = lambda : list(map(int,sys.stdin.readline().split()))
read_int_list = lambda : list(read_ints())
read = lambda : sys.stdin.readline().strip()
read_list = lambda : sys.stdin.readline().split()

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
    print(sa-sb)


main()

