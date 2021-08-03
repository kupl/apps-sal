#
# Yet I'm feeling like
# 	There is no better place than right by your side
# 		I had a little taste
# 			And I'll only spoil the party anyway
# 				'Cause all the girls are looking fine
# 					But you're the only one on my mind

from math import ceil, floor, log, sqrt, factorial, pow, pi, gcd, log10, atan, tan
import sys
# import re
inf = float("inf")
# sys.setrecursionlimit(1000000)

# abc='abcdefghijklmnopqrstuvwxyz'
# abd={'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
mod, MOD = 1000000007, 998244353
# vow=['a','e','i','o','u']
# dx,dy=[-1,1,0,0,-1,1,-1,1],[0,0,1,-1,1,1,-1,-1]

# from functools import reduce
# from collections import deque, Counter, OrderedDict,defaultdict
# from heapq import nsmallest, nlargest, heapify,heappop ,heappush, heapreplace
# from bisect import bisect_left,bisect_right,insort_left
# import numpy as np
# import queue
# from copy import deepcopy
# import random
# import operator


def get_array(): return list(map(int, sys.stdin.readline().strip().split()))
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def input(): return sys.stdin.readline().strip()


T = int(input())
while T:
    n = int(input())
    Arr = get_array()
    s = sum(Arr)
    ans = ceil(s / n)
    print(ans)
    T -= 1
