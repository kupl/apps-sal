import sys
from collections import Counter
import itertools
from math import floor, ceil


def input():
    return sys.stdin.readline().strip()


def dinput():
    return int(input())


def tinput():
    return input().split()


def rinput():
    return map(int, tinput())


def rt(x1, x2, y3):
    print(0.5 * (x2 + x1))


def main():
    y = int(input())
    i = 1
    t = 0
    r = 1
    if y % 2 == 1 and y >= 5:
        print(1, (y - 3) // 2)
    else:
        print("NO")


main()
