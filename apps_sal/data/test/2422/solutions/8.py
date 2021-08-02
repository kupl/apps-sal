import sys
import math
from collections import defaultdict, deque

input = sys.stdin.readline


def inar():
    return [int(el) for el in input().split()]


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        take = n // 3
        if n % 3 == 0:
            print(n // 3, 0, 0)
        elif n % 3 == 1:
            if (take - 2) >= 0:
                print(take - 2, 0, 1)
            else:
                print(-1)
        else:
            if (take - 1) >= 0:
                print(take - 1, 1, 0)
            else:
                print(-1)


def __starting_point():
    main()


__starting_point()
