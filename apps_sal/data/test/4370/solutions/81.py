#!/usr/bin/env python3
import sys
def input(): return sys.stdin.readline().rstrip()


def main():
    print(('Yay!' if all([True if int(x)<9 else False for x in input().split()]) else ':('))
    


def __starting_point():
    main()


__starting_point()
