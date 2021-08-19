#!/usr/bin/env python

def main():
    a1, a2, a3, a4 = list(map(int, input().split()))

    res = 0
    for s in input():
        if s == '1':
            res += a1
        if s == '2':
            res += a2
        if s == '3':
            res += a3
        if s == '4':
            res += a4

    print(res)


def __starting_point():
    main()


__starting_point()
