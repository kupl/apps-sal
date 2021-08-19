#!/usr/bin/env python3
import sys


def main():
    n = int(sys.stdin.readline())
    l = list(map(int, sys.stdin.readline().split()))
    alive = 0
    alive_indx = n
    for indx in reversed(list(range(n))):
        if alive_indx > indx:
            alive += 1
        alive_indx = min(alive_indx, indx - l[indx])
    print(alive)


def __starting_point():
    main()


__starting_point()
