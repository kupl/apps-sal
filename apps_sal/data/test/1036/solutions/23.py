import math
import sys
sys.setrecursionlimit(10 ** 7)
def getnum(t=int): return t(sys.stdin.buffer.readline())
def numline(t=int): return map(t, sys.stdin.buffer.readline().split())
def numread(t=int): return map(t, sys.stdin.buffer.read().split())
def getstr(): return sys.stdin.readline().strip()
def strline(): return sys.stdin.readline().strip().split()
def strread(): return sys.stdin.read().strip().split()


#from numba import njit, b1, i4, i8, f8, jit
#import numpy as np


def main():
    n, k, s = strread()
    N, K = int(n), int(k)
    rel = {(w, w): w for w in 'RSP'}
    rel[('R', 'S')] = 'R'
    rel[('R', 'P')] = 'P'
    rel[('S', 'P')] = 'S'
    for a, b in list(rel.keys()):
        rel[(b, a)] = rel[(a, b)]
    # print(rel)
    for k in range(K, 0, -1):
        if len(s) % 2:
            s = s + s
        next_s = ''
        for i in range(0, len(s), 2):
            next_s += rel[(s[i], s[i + 1])]
        if math.log2(len(next_s)) > k - 1:
            next_s = next_s[:2 ** (k - 1)]
        s = next_s
        # print(next_s)
    print(s[0])


def __starting_point():
    main()


__starting_point()
