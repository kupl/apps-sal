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
    A, B = numline()
    S = [list('.' * 50 + '#' * 50) for _ in range(50)]
    whites = 1
    blacks = 1
    for i in range(1, 49, 2):
        if blacks == B:
            break
        for j in range(1, 49, 2):
            if blacks == B:
                break
            S[i][j] = '#'
            blacks += 1

    for i in range(1, 49, 2):
        if whites == A:
            break
        for j in range(51, 99, 2):
            if whites == A:
                break
            S[i][j] = '.'
            whites += 1

    print(50, 100)
    for s in S:
        print(''.join(s))


def __starting_point():
    main()


__starting_point()
