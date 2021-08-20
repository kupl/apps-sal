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
    (N, M) = NMI()
    AB = [NLI() for _ in range(N)]
    CD = [NLI() for _ in range(M)]
    for n in range(N):
        A = AB[n][0]
        B = AB[n][1]
        distance = []
        for m in range(M):
            C = CD[m][0]
            D = CD[m][1]
            distance.append(abs(A - C) + abs(B - D))
        print(distance.index(min(distance)) + 1)


def __starting_point():
    main()


__starting_point()
