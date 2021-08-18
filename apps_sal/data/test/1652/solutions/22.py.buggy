from itertools import accumulate, permutations, combinations, product, combinations_with_replacement
from math import floor, ceil, sqrt, factorial, log
from collections import Counter, defaultdict, deque
from bisect import bisect_left, bisect_right
from fractions import gcd
from operator import itemgetter
from copy import deepcopy
from heapq import heappop, heappush, heappushpop
import sys
sys.setrecursionlimit(10**6)
mod = 10 ** 9 + 7
inf = float('inf')
ninf = -float('inf')

# 整数input


def ii(): return int(sys.stdin.readline().rstrip())  # int(input())
def mii(): return map(int, sys.stdin.readline().rstrip().split())
def limii(): return list(mii())  # list(map(int,input().split()))
def lin(n: int): return [ii() for _ in range(n)]
def llint(n: int): return [limii() for _ in range(n)]
# 文字列input
def ss(): return sys.stdin.readline().rstrip()  # input()
def mss(): return sys.stdin.readline().rstrip().split()
def limss(): return list(mss())  # list(input().split())
def lst(n: int): return [ss() for _ in range(n)]
def llstr(n: int): return [limss() for _ in range(n)]

# 本当に貪欲法か？ DP法では？？
# 本当に貪欲法か？ DP法では？？
# 本当に貪欲法か？ DP法では？？


s = list(ss())
lens = len(s)
flag = True

s.reverse()

word = ("maerd", "remaerd", "esare", "resare")

cnt = 0

while cnt < lens:
    cnt_chk = cnt
    if "".join(s[cnt:cnt + 5]) == word[0]:
        cnt_chk += 5
    elif "".join(s[cnt:cnt + 7]) == word[1]:
        cnt_chk += 7
    elif "".join(s[cnt:cnt + 5]) == word[2]:
        cnt_chk += 5
    elif "".join(s[cnt:cnt + 6]) == word[3]:
        cnt_chk += 6
    if cnt == cnt_chk:
        print("NO")
        return
    else:
        cnt = cnt_chk
print("YES")
