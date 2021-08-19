import math
import itertools
import fractions
import heapq
import collections
import bisect
import sys
import queue
import copy

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI(): return [int(x) for x in sys.stdin.readline().split()]
# def LF(): return [float(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()


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
            else:
                if s[i] == 'o':
                    ind = a.index(ans[i - 1])
                    ans.append(a[1 - ind])
                else:
                    ans.append(ans[i - 1])
        stress = ''.join(str(x) for x in ans)
        f = True
        for i in range(N):
            if stress[i] == 'S':
                if i == 0:
                    if s[i] == 'o':
                        if not (stress[-1] == stress[i + 1]):
                            # return 'aaa1'+' '+stress
                            f = False
                    else:
                        if not (stress[-1] != stress[i + 1]):
                            # return 'aaa2'
                            f = False
                elif i == N - 1:
                    if s[i] == 'o':
                        if not (stress[i - 1] == stress[0]):
                            # return 'aaa3'
                            f = False
                    else:
                        if not (stress[i - 1] != stress[0]):
                            # return 'aaa4'
                            f = False
                else:
                    if s[i] == 'o':
                        if not (stress[i - 1] == stress[i + 1]):
                            # return 'aaa5'
                            f = False
                    else:
                        if not (stress[i - 1] != stress[i + 1]):
                            # return 'aaa6'
                            f = False
            else:
                if i == 0:
                    if s[i] == 'o':
                        if not (stress[-1] != stress[i + 1]):
                            # return 'bbb1'
                            f = False
                    else:
                        if not (stress[-1] == stress[i + 1]):
                            # return 'bbb2'
                            f = False
                elif i == N - 1:
                    if s[i] == 'o':
                        if not (stress[i - 1] != stress[0]):
                            # return 'bbb3'
                            f = False
                    else:
                        if not (stress[i - 1] == stress[0]):
                            # return 'bbb4'
                            f = False
                else:
                    if s[i] == 'o':
                        if not (stress[i - 1] != stress[i + 1]):
                            # return 'bbb5'
                            f = False
                    else:
                        if not (stress[i - 1] == stress[i + 1]):
                            # return 'bbb6'
                            f = False

        if f:
            return ''.join(str(x) for x in ans)

    return -1


# main()
print((main()))
