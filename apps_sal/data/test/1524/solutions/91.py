import re
import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
import functools
def v(): return input()
def k(): return int(input())
def S(): return input().split()
def I(): return list(map(int,input().split()))
def X(): return list(input())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 9)
mod = 10**9+7
cnt = 0
ans = 0
inf = float("inf")
al = "abcdefghijklmnopqrstuvwxyz"
AL = al.upper()

s = v()
a = len(s)
p = [0]*a
check = True
now_before = 0
now_after = 0
cnt_x = 1
cnt_y = 0

for i in range(1,a):
    if s[i] == "L" and check == True:
        now_before = i-1
        now_after = i
        check = False
        if i % 2 == 0:
            p[now_before] += cnt_y
            p[now_after] += cnt_x+1
        else:
            p[now_before] += cnt_x
            p[now_after] += cnt_y+1
        cnt_x = 0
        cnt_y = 0
    elif s[i] == "L" and check == False:
        if (i - now_after) % 2 == 0:
            p[now_after] += 1
        else:
            p[now_before] += 1   
    elif s[i] == "R" and check == False:
        check = True
        if i%2==0:
            cnt_x += 1
        else:
            cnt_y += 1
    elif s[i] == "R" and check == True:
        if i%2==0:
            cnt_x += 1
        else:
            cnt_y += 1

print((" ".join(map(str,p))))



