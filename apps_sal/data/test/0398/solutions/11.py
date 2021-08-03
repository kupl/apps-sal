import math
import sys
import itertools


def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n - 2):
        if a[i] + a[i + 1] > a[i + 2]:
            print('YES')
            return
    print('NO')


def __starting_point():
    main()


__starting_point()
