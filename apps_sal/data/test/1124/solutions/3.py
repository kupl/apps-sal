import sys
import math
import itertools
from collections import defaultdict, deque, Counter
from copy import deepcopy
from bisect import bisect, bisect_right, bisect_left
from heapq import heapify, heappop, heappush
from operator import itemgetter, attrgetter

input = sys.stdin.readline
def RD(): return input().rstrip()
def F(): return float(input().rstrip())
def I(): return int(input().rstrip())
def MI(): return map(int, input().split())
def MF(): return map(float, input().split())
def LI(): return list(map(int, input().split()))
def TI(): return tuple(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def Init(H, W, num): return [[num for i in range(W)] for j in range(H)]
def TL(mylist): return [list(x) for x in zip(*mylist)]
def RtoL(mylist): return [list(reversed(x)) for x in mylist]
def HtoL(mylist): return [x for x in list(reversed(mylist))]
def convert_2d(l, colstart, colend, rawstart, rawend): return [i[rawstart:rawend] for i in l[colstart:colend]]


def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]


def main():
    N = I()
    L = LI()
    ans = L[0]
    for i in range(N):
        temp = L[i]
        ans = math.gcd(ans, temp)
    print(ans)


def __starting_point():
    main()


__starting_point()
