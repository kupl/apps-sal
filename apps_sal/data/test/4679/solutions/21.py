import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from bisect import bisect, bisect_left, bisect_right

def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def S_MAP(): return list(map(str, input().split()))
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
 
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

A = deque(list(input()))
B = deque(list(input()))
C = deque(list(input()))

# while len(A) == 0 or len(B) == 0 or len(C) == 0:
p = A.popleft()
while 1:
    if p == "a":
        if len(A) == 0:
            print("A")
            return
        else:
            p = A.popleft()
    if p == "b":
        if len(B) == 0:
            print("B")
            return
        else:
            p = B.popleft()

    if p == "c":
        if len(C) == 0:
            print("C")
            return
        else:
            p = C.popleft()
    
    


