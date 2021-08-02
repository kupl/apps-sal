import sys
import os


def turnTheRectangles(rects):
    last = 10**10
    for rect in rects:
        a = max(rect[0], rect[1])
        b = min(rect[0], rect[1])
        if a <= last:
            last = a
        elif b <= last:
            last = b
        else:
            return 'NO'
    return 'YES'


def main():
    n = int(input())
    rects = []
    for i in range(n):
        w, h = (int(x) for x in input().split())
        rects.append([w, h])
    print(turnTheRectangles(rects))


def __starting_point():
    main()


__starting_point()
