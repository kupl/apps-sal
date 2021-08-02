#!/usr/bin/env python3
import sys


def input():
    return sys.stdin.readline()[:-1]


def main():
    H, W = list(map(int, input().split()))
    a = []
    white = '.' * W
    for i in range(H):
        s = input()
        if s == white:
            pass
        else:
            a.append(s)

    black = []
    for w in range(W):
        for h in range(len(a)):
            if a[h][w] == '#':
                black.append(w)

    black = sorted(list(set(black)))
    for h in range(len(a)):
        t = ''
        for b in black:
            t += a[h][b]
        print(t)


def __starting_point():
    main()


__starting_point()
