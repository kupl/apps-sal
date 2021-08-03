import sys
import math
import itertools
import collections
from collections import deque
from collections import defaultdict
import copy

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
    H, W, K = NMI()

    C = [list(input()) for _ in range(H)]

    ans = 0

    for hi in range(2**H):
        for wi in range(2**W):
            CC = copy.deepcopy(C)

            for hj in range(H):
                if (hi >> hj) & 1:
                    for x in range(W):
                        CC[hj][x] = "R"

            for wj in range(W):
                if (wi >> wj) & 1:
                    for x in range(H):
                        CC[x][wj] = "R"

            cnt = 0
            for h in range(H):
                cnt += CC[h].count("#")

            if cnt == K:
                ans += 1

    print(ans)


def __starting_point():
    main()


__starting_point()
