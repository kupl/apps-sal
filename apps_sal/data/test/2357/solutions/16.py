from heapq import heappush, heappop
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations
import sys
import bisect
import string


def I():
    return int(input())


def MI():
    return map(int, input().split())


def LI():
    return [int(i) for i in input().split()]


def LI_():
    return [int(i) - 1 for i in input().split()]


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


YN = ['Yes', 'No']
mo = 10**9 + 7
inf = float('inf')

input = sys.stdin.readline
show_flg = False
show_flg = True

t = I()
for _ in range(t):
    n = I()
    a = LI()
    p = [-1] * (1 + n)
    ans = inf
    for i in range(n):
        if p[a[i]] != -1:
            ans = min(ans, i - p[a[i]] + 1)
        p[a[i]] = i
    if ans == inf:
        ans = -1
    print(ans)
