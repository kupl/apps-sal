#!/usr/bin/env python3


def are_same(a, b):
    a = a.lower()
    b = b.lower()
    if a == b:
        return True
    if a in {'o', '0'}:
        return b in {'o', '0'}
    if a in {'1', 'l', 'i'}:
        return b in {'1', 'l', 'i'}


def main():
    s = input()
    n = int(input())
    for _ in range(n):
        s1 = input()

        if len(s1) == len(s) and all(are_same(x1, x2) for x1, x2 in zip(s, s1)):
            print('No')
            return
    print('Yes')


def __starting_point():
    main()


__starting_point()
