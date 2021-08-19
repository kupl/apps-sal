#
# Yet I'm feeling like
# 	There is no better place than right by your side
# 		I had a little taste
# 			And I'll only spoil the party anyway
# 				'Cause all the girls are looking fine
# 					But you're the only one on my mind


import sys
import re
# inf = float("inf")
# sys.setrecursionlimit(1000000)

# abc='abcdefghijklmnopqrstuvwxyz'
# abd={'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
# mod,MOD=1000000007,998244353
# vow=['a','e','i','o','u']
# dx,dy=[-1,1,0,0],[0,0,1,-1]

# from cmath import sqrt
from collections import deque, Counter, OrderedDict, defaultdict
from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
# from math import ceil,floor,log,sqrt,factorial,pow,pi,gcd,log10,atan,tan
from bisect import bisect_left, bisect_right
# import numpy as np


def dfs(curr, parent):
    visited[curr] = True
    value[curr] += value[parent]
    for i in mydict[curr]:
        if not visited[i]:
            dfs(i, curr)


def get_array(): return list(map(int, sys.stdin.readline().strip().split()))
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def input(): return sys.stdin.readline().strip()


n = int(input())
A = get_array()
A.sort()
m = int(input())
B = get_array()
B.sort()
print(A[-1], B[-1])
