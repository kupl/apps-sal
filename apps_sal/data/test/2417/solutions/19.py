from heapq import heappush, heappop
from collections import deque, defaultdict, Counter
import itertools
from itertools import permutations, combinations
import sys
import bisect
import string
#import math
#import time
# import random  # randome is not available at Codeforces


def I():
    return int(input())


def MI():
    return map(int, input().split())


def LI():
    return [int(i) for i in input().split()]


def LI_():
    return [int(i) - 1 for i in input().split()]


def StoI():
    return [ord(i) - 97 for i in input()]


def show(*inp, end='\n'):
    if show_flg:
        print(*inp, end=end)


YN = ['Yes', 'No']
mo = 10**9 + 7
inf = float('inf')
# ts=time.time()
# sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10**7)

show_flg = False
# show_flg=True


n = I()
en = LI()[::-1]
ex = LI()[::-1]

show(en, ex)
ans = 0
f = [0] * (n + 1)
while en:
    c = en.pop()
    if f[c] == 1:
        continue
    while ex:
        d = ex.pop()
        if d == c:
            break
        ans += 1
        f[d] = 1
        show(c, d, en, ex)

print(ans)

show(f)
