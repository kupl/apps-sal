#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    n, pos, l, r = [int(_) for _ in input().split(' ')]
    if l is 1 and r == n:
        print(0)
        return
    if l is 1:
        print(abs(r - pos) + 1)
        return
    if r == n:
        print(abs(l - pos) + 1)
        return
    print(min(abs(l - pos), abs(r - pos)) + (r - l) + 2)


main()
