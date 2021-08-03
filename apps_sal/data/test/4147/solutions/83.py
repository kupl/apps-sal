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


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N, A, B, C = NMI()
    L = [NI() for _ in range(N)]

    def dfs(bamboo, a, b, c):
        if bamboo == N:
            if a * b * c == 0:
                return 10**100
            a, b, c = sorted([a, b, c], reverse=True)
            res = abs(A - a) + abs(B - b) + abs(C - c)
            return res

        res = 10**100

        res = min(res, dfs(bamboo + 1, a + L[bamboo], b, c) + 10) if a > 0 else min(res, dfs(bamboo + 1, a + L[bamboo], b, c))
        res = min(res, dfs(bamboo + 1, a, b + L[bamboo], c) + 10) if b > 0 else min(res, dfs(bamboo + 1, a, b + L[bamboo], c))
        res = min(res, dfs(bamboo + 1, a, b, c + L[bamboo]) + 10) if c > 0 else min(res, dfs(bamboo + 1, a, b, c + L[bamboo]))
        res = min(res, dfs(bamboo + 1, a, b, c))
        return res

    print(dfs(0, 0, 0, 0))


def __starting_point():
    main()


__starting_point()
