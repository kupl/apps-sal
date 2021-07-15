# -*- coding: utf-8 -*-
import numpy as np
import sys
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect

sys.setrecursionlimit(10**6)
def zz():
    return list(map(int, sys.stdin.readline().split()))


def z():
    return int(sys.stdin.readline())


def S():
    return sys.stdin.readline()


def C(line):
    return [sys.stdin.readline() for _ in range(line)]

def nck(n, k, mod=10**9+7):
    bunbo = bunshi = 1
    for i in range(k):
        bunshi = (bunshi * (n-i)) % mod
        bunbo = (bunbo * (i+1)) % mod
    return (bunshi * pow(bunbo, mod-2, mod)) % mod

N,K=zz()
ans = 0
modK = 0
if (K % 2 == 0):
    mod0 = N//K
    ans += mod0**3
    a = (N + K//2)//K
    # print(a)
    ans+=a**3
else:
    mod0 = N // K
    ans=mod0**3
print(ans)
