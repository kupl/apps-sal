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
input = lambda: sys.stdin.readline().strip()

NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, K = NMI()
    A = NLI()

    ng = 0  # ng:とり得る最小の値-1
    ok = 10**9 + 10  # ok:とり得る最大の値+1

    while (abs(ok - ng) > 1):
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
