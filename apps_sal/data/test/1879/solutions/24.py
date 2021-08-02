#!/usr/bin/env python3
#! -*- coding: utf-8 -*-


def main():
    t, sx, sy, ex, ey = list(map(int, input().split()))
    path = input()
    dx, dy = ex - sx, ey - sy
    if not dx and not dy:
        print(0)
        return
    for i, move in enumerate(path):
        #print(dx, dy)
        if dx < 0 and move == 'W':
            dx += 1
        elif dx > 0 and move == 'E':
            dx -= 1
        elif dy < 0 and move == 'S':
            dy += 1
        elif dy > 0 and move == 'N':
            dy -= 1
        if not dx and not dy:
            print(i + 1)
            break
    else:
        print("-1")


def __starting_point():
    main()


__starting_point()
