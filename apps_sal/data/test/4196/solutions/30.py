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


def input():
    return sys.stdin.readline().strip()


def NI():
    return int(input())


def NMI():
    return map(int, input().split())


def NLI():
    return list(NMI())


def SI():
    return input()


def main():
    N = NI()
    A = NLI()
    L = [0 for _ in range(N)]
    L_gcd = 0
    for n in range(0, N - 1):
        L_gcd = math.gcd(A[n], L_gcd)
        L[n + 1] = L_gcd
    R = [0 for _ in range(N)]
    R_gcd = 0
    for n in range(N - 1, -1, -1):
        R_gcd = math.gcd(A[n], R_gcd)
        R[n - 1] = R_gcd
    R[-1] = 0
    ans = 0
    for n in range(N):
        ans = max(ans, math.gcd(L[n], R[n]))
    print(ans)


def __starting_point():
    main()


__starting_point()
