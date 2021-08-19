import sys
import threading
import os.path
import collections
import heapq
import math
import bisect
import string
from platform import python_version
sys.setrecursionlimit(10 ** 6)
threading.stack_size(2 ** 27)


def main():
    if os.path.exists('input.txt'):
        input = open('input.txt', 'r')
    else:
        input = sys.stdin
    (t, x1, x2, y1, y2) = list(map(int, input.readline().split()))
    T = t
    dirs = list(str(input.readline().rstrip('\n')))
    for i in range(len(dirs)):
        if t == 0 or (x1 == y1 and x2 == y2):
            break
        if dirs[i] == 'E':
            if y1 > x1:
                x1 += 1
            t -= 1
        elif dirs[i] == 'S':
            if x2 > y2:
                x2 -= 1
            t -= 1
        elif dirs[i] == 'W':
            if y1 < x1:
                x1 -= 1
            t -= 1
        elif dirs[i] == 'N':
            if x2 < y2:
                x2 += 1
            t -= 1
    if x1 == y1 and x2 == y2:
        output = T - t
    else:
        output = -1
    if os.path.exists('output.txt'):
        open('output.txt', 'w').writelines(str(output))
    else:
        sys.stdout.write(str(output))


def __starting_point():
    main()


__starting_point()
