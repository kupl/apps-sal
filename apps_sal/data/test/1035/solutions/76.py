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
    GCD = math.gcd(A, B)
    N = GCD

    cnt = 0

    ls = []

    for n in range(2, int(N**0.5) + 2):

        if GCD % n == 0:
            cnt += 1

            while GCD % n == 0:
                GCD = GCD // n
                ls.append(n)

    if GCD == 1:
        print(cnt + 1)
    else:
        print(cnt + 2)


def __starting_point():
    main()


__starting_point()
