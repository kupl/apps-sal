import math
import sys
from collections import defaultdict
input = sys.stdin.readline


def main():
    t = int(input())
    for _ in range(t):
        ni = int(input())
        cnt3 = 2
        while (cnt3 * (cnt3 + 1)) // 2 <= ni:
            cnt3 += 1
        rest = ni - (cnt3 * (cnt3 - 1) // 2)
        print('1' + '33' + '7' * rest + '3' * (cnt3 - 2) + '7')


def __starting_point():
    main()


__starting_point()
