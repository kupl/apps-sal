import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    L = SI()
    keta = len(L)

    def rec(n):
        if n == 1:
            return 3 if L[keta - n] == "1" else 1

        if L[keta - n] == "1":
            return (pow(3, (n-1), MOD) + rec(n-1) * 2) % MOD
        else:
            return rec(n-1) % MOD

    print(rec(keta))


def __starting_point():
    main()
__starting_point()
