import sys
import math
import itertools
import collections
from collections import deque
from collections import defaultdict

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD2 = 998244353
INF = float('inf')
def input(): return sys.stdin.readline().strip()


def NI(): return int(input())
def NMI(): return map(int, input().split())
def NLI(): return list(NMI())
def SI(): return input()


def main():
    N = NI()
    A = NLI()
    B = NLI()
    C = NLI()

    A = sorted(A)
    C = sorted(C)

    ans = 0

    for b in B:

        A_ng = -1
        A_ok = len(A)

        while (abs(A_ok - A_ng) > 1):
            A_mid = (A_ok + A_ng) // 2

            if A[A_mid] >= b:
                A_ok = A_mid
            else:
                A_ng = A_mid

        C_ng = -1
        C_ok = len(C)

        while (abs(C_ok - C_ng) > 1):
            C_mid = (C_ok + C_ng) // 2

            if C[C_mid] > b:
                C_ok = C_mid
            else:
                C_ng = C_mid

        len_C = len(C)

        ans += A_ok * (len_C - C_ok)

    print(ans)


def __starting_point():
    main()


__starting_point()
