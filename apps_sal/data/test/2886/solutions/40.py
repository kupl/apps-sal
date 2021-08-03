import sys
import numpy as np
import random
from decimal import Decimal
import itertools
import re
import bisect
from collections import deque, Counter
from functools import lru_cache

sys.setrecursionlimit(10**9)
INF = 10**13
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
def SERIES(n): return np.fromstring(sys.stdin.buffer.read(), dtype=np.int32, sep=' ')
def GRID(h, w): return np.fromstring(sys.stdin.buffer.read(), dtype=np.int32, sep=' ').reshape(h, -1)[:, :w]
def GRIDfromString(h, w): return np.frombuffer(sys.stdin.buffer.read(), 'S1').reshape(h, -1)[:, :w]


MOD = 1000000007


def main():
    s_list = list(S())
    for t in range(2, min(len(s_list) + 1, 4)):
        for i in range(len(s_list) - t + 1):
            c = Counter(s_list[i:i + t])
            if c.most_common()[0][1] / t > 0.5:
                print(i + 1, i + t)
                break
        else:
            continue
        break
    else:
        print(-1, -1)


def __starting_point():
    main()


__starting_point()
