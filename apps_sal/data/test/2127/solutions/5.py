

import sys

inf = float("inf")
mod = 1000000007


def get_array(): return list(map(int, sys.stdin.readline().split()))


def get_ints(): return list(map(int, sys.stdin.readline().split()))


def input(): return sys.stdin.readline()


def main():
    h, w = 0, 0
    for tc in range(int(input())):
        t, x, y = input().split()
        x = int(x)
        y = int(y)
        if x < y:
            x, y = y, x
        if t == '+':
            h = max(h, x)
            w = max(w, y)
        elif t == '?':
            if x >= h and y >= w:
                print('YES')
            else:
                print('NO')


def __starting_point():
    main()


__starting_point()
