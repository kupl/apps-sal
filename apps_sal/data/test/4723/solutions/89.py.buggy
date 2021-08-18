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

S = v()
T = v()
len_s = len(S)
len_t = len(T)
check = False
ans = []

if len_s < len_t:
    print("UNRESTORABLE")
    return

for i in range(len_s):
    if S[i] == "?":
        cnt += 1
        if cnt >= len_t:
            aaa = S.replace("?", "a")
            ans.append(aaa[:i - len_t + 1] + T + aaa[i + 1:])
    elif S[i] in T:
        cnt = 0
        place = T.index(S[i])
        if len_s < len_t + i - place:
            break
        for j in range(i - place, len_t + i - place):
            if T[j - (i - place)] == S[j] or S[j] == "?":
                check = True
            else:
                check = False
                break
        if check:
            aaa = S.replace("?", "a")
            ans.append(aaa[:i - place] + T + aaa[len_t + i - place:])
    else:
        cnt = 0

if len(ans) > 0:
    ans.sort()
    print((ans[0]))
else:
    print("UNRESTORABLE")
