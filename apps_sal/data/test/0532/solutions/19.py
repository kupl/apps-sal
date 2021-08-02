#!/usr/bin/env python3

SEQ = 'abcdefghijklmnopqrstuvwxyz'


def dist(a, b):
    a = ord(a) - ord('a')
    b = ord(b) - ord('a')
    d = abs(a - b)
    return min(d, 26 - d)


def __starting_point():
    seq = input()
    pos = 'a'
    r = 0
    for c in seq:
        r += dist(pos, c)
        pos = c
    print(r)


__starting_point()
