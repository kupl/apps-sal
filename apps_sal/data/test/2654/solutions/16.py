#!/usr/bin/env python3
# encoding:utf-8
import copy
import random
import bisect #bisect_left　これで二部探索の大小検索が行える
import fractions #最小公倍数などはこっち
import math
import sys
import collections

mod = 10**9+7
sys.setrecursionlimit(mod) # 再帰回数上限はでdefault1000

d = collections.deque()
def LI(): return list(map(int, sys.stdin.readline().split()))

N = int(input())
A = [0 for i in range(N)]
B = [0 for i in range(N)]
for i in range(N):
    a,b = LI()
    A[i] = a
    B[i] = b

A.sort()
B.sort()

if N % 2 == 1:
    min_mid = A[(N - 1) // 2]
else:
    min_mid = (A[N //2 - 1] + A[N//2]) / 2

if N % 2 == 1:
    max_mid = B[(N - 1) // 2]
else:
    max_mid = (B[N //2 - 1] + B[N//2]) / 2 

if N % 2 == 0:
    print((int((max_mid - min_mid) / 0.5 + 1)))
else:
    print((math.ceil(max_mid) - math.floor(min_mid) + 1))



