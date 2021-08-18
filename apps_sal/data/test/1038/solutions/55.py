import sys
import math
import itertools
import collections
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
def input(): return sys.stdin.readline().strip()


def NI(): return int(input())
def NMI(): return map(int, input().split())
def NLI(): return list(NMI())
def SI(): return input()


def main():
    A, B = NMI()

    xA, xB = 0, 0

    if A == 0 or A == 1:
        xA = 0
    else:
        if A % 4 == 1:
            xA = A - 1
        elif A % 4 == 2:
            xA = 1
        elif A % 4 == 3:
            xA = A
        else:
            xA = 0

    if B == 0:
        xB = 0
    else:
        if B % 4 == 1:
            xB = 1
        elif B % 4 == 2:
            xB = B + 1
        elif B % 4 == 3:
            xB = 0
        else:
            xB = B

    A_bin = format(xA, '040b')
    B_bin = format(xB, '040b')

    ans = ['0' for _ in range(40)]

    for i in range(39, -1, -1):
        if int(A_bin[i]) + int(B_bin[i]) == 1:
            ans[i] = '1'

    print(int("".join(ans), 2))


def __starting_point():
    main()


__starting_point()
