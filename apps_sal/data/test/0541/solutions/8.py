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
    N, M = NMI()
    ab = [NLI() for _ in range(M)]

    ENDsorted_sections = sorted(ab, key=lambda x: x[1])

    ans = 1
    dropped_bridge = ENDsorted_sections[0][1]

    for m in range(M):
        if ENDsorted_sections[m][0] >= dropped_bridge:
            ans += 1
            dropped_bridge = ENDsorted_sections[m][1]
    print(ans)


def __starting_point():
    main()


__starting_point()
