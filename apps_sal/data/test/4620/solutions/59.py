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
    CSF = [NLI() for _ in range(N - 1)]
    CSF.append([0, 0, 1])

    for n in range(N - 1):
        time = CSF[n][1]

        for m in range(n, N - 1):
            time += CSF[m][0]
            if time < CSF[m + 1][1]:
                time = CSF[m + 1][1]
            else:
                if time % CSF[m + 1][2] != 0:
                    time = ((time // CSF[m + 1][2]) + 1) * CSF[m + 1][2]
        print(time)
    print(0)


def __starting_point():
    main()


__starting_point()
