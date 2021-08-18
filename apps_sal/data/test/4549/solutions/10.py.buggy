import re
import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque, Counter
from decimal import Decimal
import functools
def v(): return input()
def k(): return int(input())
def S(): return input().split()
def I(): return list(map(int, input().split()))
def X(): return list(input())
def L(): return list(input().split())
def l(): return list(map(int, input().split()))
def lcm(a, b): return a * b // math.gcd(a, b)


sys.setrecursionlimit(10 ** 6)
mod = 10**9 + 7
cnt = 0
ans = 0
inf = float("inf")
al = "abcdefghijklmnopqrstuvwxyz"
AL = al.upper()

H, W = I()

pad_s = ['.' * (W + 2)]
for h in range(H):
    pad_s.append('.' + input() + '.')
pad_s.append('.' * (W + 2))

for i, ss in enumerate(pad_s):
    for j, s in enumerate(ss):
        if s == '#'\
                and pad_s[i][j + 1] == '.'\
                and pad_s[i][j - 1] == '.'\
                and pad_s[i + 1][j] == '.'\
                and pad_s[i - 1][j] == '.':
            print('No')
            return

print('Yes')
