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
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()


def main():
    n, k = LI()
    v = LI()

    ans = 0
    for i in range(k):
        if i + 1 < n:
            for l in range(i + 1):
                r = i - l

                _ans = 0
                _v = []
                for x in range(l + 1):
                    _ans += v[x]
                    _v.append(v[x])
                for x in range(r):
                    _ans += v[n - x - 1]
                    _v.append(v[n - x - 1])

                _v.sort()
                for j in range(min(len(_v), k - i - 1)):
                    if _v[j] < 0:
                        _ans -= _v[j]
                    else:
                        break
                ans = max(ans, _ans)
        else:
            _v = v.sort()
            _ans = sum(v)
            _k = n - k - 1
            for j in range(_k):
                if _v[j] < 0:
                    _ans -= _v[j]
                else:
                    break
            ans = max(ans, _ans)

    return ans


print((main()))
