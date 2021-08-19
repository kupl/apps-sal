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
    (N, K) = NMI()
    A = NLI()
    ng = 0
    ok = 10 ** 9 + 10
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        cut = 0
        for a in A:
            if a % mid == 0:
                cut += math.floor(a / mid) - 1
            else:
                cut += math.floor(a / mid)
        if cut <= K:
            ok = mid
        else:
            ng = mid
    print(ok)


def __starting_point():
    main()


__starting_point()
