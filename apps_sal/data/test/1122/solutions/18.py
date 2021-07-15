from collections import deque
from itertools import product
import sys
import math

sys.setrecursionlimit(200000)
input = sys.stdin.readline


def read():
    N, M = list(map(int, input().strip().split()))
    return N, M


def solve(N, M):
    H = (N-1) // 2
    LL = 0
    LR = (H // 2) * 2 + 1
    RL = N - (H - H//2) * 2
    RR = N
    pairs = []
    while LR - LL > 1:
        pairs.append((LL+1, LR))
        LL += 1
        LR -= 1
    while RR - RL > 1:
        pairs.append((RL+1, RR))
        RL += 1
        RR -= 1
    for i in range(M):
        print((*pairs[i]))


def __starting_point():
    inputs = read()
    solve(*inputs)

__starting_point()
