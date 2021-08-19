import sys
import heapq as hq
import itertools
import math
import collections
def ma(): return map(int, input().split())
def lma(): return list(map(int, input().split()))
def tma(): return tuple(map(int, input().split()))
def ni(): return int(input())
def yn(fl): return print("Yes") if fl else print("No")


h, w = ma()
t = "." * w
ls = []
for i in range(h):
    s = input()
    if s != t:
        ls.append(s)

l = len(ls)
t = "." * l
ans = [[] for i in range(l)]
for i in range(w):
    f = False
    for j in range(l):
        if ls[j][i] == "#":
            f = True
    if f:
        for j in range(l):
            ans[j].append(ls[j][i])
for a in ans:
    print("".join(a))
