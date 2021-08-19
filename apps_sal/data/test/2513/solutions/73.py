import math
import itertools
import fractions
import heapq
import collections
import bisect
import sys
import queue
import copy
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20
mod = 10 ** 9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI():
    return [int(x) for x in sys.stdin.readline().split()]


def I():
    return int(sys.stdin.readline())


def F():
    return float(sys.stdin.readline())


def LS():
    return sys.stdin.readline().split()


def S():
    return input()


def main():
    N = I()
    s = S()
    a = ['S', 'W']
    aa = (['S', 'S'], ['S', 'W'], ['W', 'S'], ['W', 'W'])
    for ans in aa:
        for i in range(1, N - 1):
            if ans[i] == 'S':
                if s[i] == 'o':
                    ans.append(ans[i - 1])
                else:
                    ind = a.index(ans[i - 1])
                    ans.append(a[1 - ind])
            elif s[i] == 'o':
                ind = a.index(ans[i - 1])
                ans.append(a[1 - ind])
            else:
                ans.append(ans[i - 1])
        stress = ''.join((str(x) for x in ans))
        f = True
        for i in range(N):
            if stress[i] == 'S':
                if i == 0:
                    if s[i] == 'o':
                        if not stress[-1] == stress[i + 1]:
                            f = False
                    elif not stress[-1] != stress[i + 1]:
                        f = False
                elif i == N - 1:
                    if s[i] == 'o':
                        if not stress[i - 1] == stress[0]:
                            f = False
                    elif not stress[i - 1] != stress[0]:
                        f = False
                elif s[i] == 'o':
                    if not stress[i - 1] == stress[i + 1]:
                        f = False
                elif not stress[i - 1] != stress[i + 1]:
                    f = False
            elif i == 0:
                if s[i] == 'o':
                    if not stress[-1] != stress[i + 1]:
                        f = False
                elif not stress[-1] == stress[i + 1]:
                    f = False
            elif i == N - 1:
                if s[i] == 'o':
                    if not stress[i - 1] != stress[0]:
                        f = False
                elif not stress[i - 1] == stress[0]:
                    f = False
            elif s[i] == 'o':
                if not stress[i - 1] != stress[i + 1]:
                    f = False
            elif not stress[i - 1] == stress[i + 1]:
                f = False
        if f:
            return ''.join((str(x) for x in ans))
    return -1


print(main())
