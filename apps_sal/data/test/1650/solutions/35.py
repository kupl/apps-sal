import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
def input(): return sys.stdin.readline().strip()
def NI(): return int(input())
def NMI(): return map(int, input().split())
def NLI(): return list(NMI())
def SI(): return input()


def main():
    L = SI()
    keta = len(L)

    def rec(n):
        if n == 1:
            return 3 if L[keta - n] == "1" else 1

        if L[keta - n] == "1":
            return (pow(3, (n - 1), MOD) + rec(n - 1) * 2) % MOD
        else:
            return rec(n - 1) % MOD

    print(rec(keta))


def __starting_point():
    main()


__starting_point()
