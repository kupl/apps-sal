import bisect
import collections
import copy
import heapq
import itertools
import math
import string
import sys
def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10**7)
INF = float('inf')
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x) - 1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()


def resolve():
    N, A, B, C = LI()
    ABC = (A, B, C)
    l = [I() for _ in range(N)]

    # A, B, Cに使う、捨てる、の4通り
    ans = INF
    for i in itertools.product(list(range(4)), repeat=N):
        a_cnt = i.count(0)
        b_cnt = i.count(1)
        c_cnt = i.count(2)
        if a_cnt > 0 and b_cnt > 0 and c_cnt > 0:
            # 合成魔法
            mp = 10 * (a_cnt + b_cnt + c_cnt - 3)
            # 延長短縮魔法
            len = [0] * 3
            for j in range(N):
                if 0 <= i[j] < 3:
                    len[i[j]] += l[j]
            mp += sum([abs(j - k) for j, k in zip(ABC, len)])
            ans = min(mp, ans)

    print(ans)


def __starting_point():
    resolve()


__starting_point()
