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
    X, Y, Z, K = NMI()
    A = NLI()
    B = NLI()
    C = NLI()
    AB = []
    for a in A:
        for b in B:
            AB.append(a + b)
    AB.sort(reverse=True)
    C.sort(reverse=True)
    S = []
    for c_idx in range(min(len(C), 3000)):
        for ab_idx in range(min(len(AB), 3000)):
            S.append(C[c_idx] + AB[ab_idx])
    S.sort(reverse=True)
    for i in range(K):
        print(S[i])


def __starting_point():
    main()


__starting_point()
