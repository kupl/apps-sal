# import sys
# input = sys.stdin.readline
import math
import copy
import bisect
from itertools import accumulate
from collections import Counter, defaultdict, deque
def mp(): return list(map(int, input().split()))
def lmp(): return list(map(int, input().split()))
def ceil(U, V): return (U + V - 1) // V
def modf1(N, MOD): return (N - 1) % MOD + 1


n = int(input())
t = input()
if n == 1:
    if t == "0":
        print((int(1e10)))
        return
    else:
        print((int(2e10)))
        return
if n == 2:
    if t == "11" or t == "10":
        print((int(1e10)))
        return
    elif t == "01":
        print((int(1e10 - 1)))
        return
    else:
        print((0))
        return

if t[:3] == "110":
    if n % 3 == 0:
        if t != "110" * (n // 3):
            print((0))
            return
    elif n % 3 == 1:
        if t != "110" * (n // 3) + "1":
            print((0))
            return
    elif n % 3 == 2:
        if t != "110" * (n // 3) + "11":
            print((0))
            return
    print((int(1e10) - ceil(n, 3) + 1))

elif t[:3] == "101":
    if n % 3 == 0:
        if t != "101" * (n // 3):
            print((0))
            return
        print((int(1e10) - ceil(n, 3)))
    elif n % 3 == 1:
        if t != "101" * (n // 3) + "1":
            print((0))
            return
        print((int(1e10) - ceil(n, 3) + 1))
    elif n % 3 == 2:
        if t != "101" * (n // 3) + "10":
            print((0))
            return
        print((int(1e10) - ceil(n, 3) + 1))

elif t[:3] == "011":
    if n % 3 == 0:
        if t != "011" * (n // 3):
            print((0))
            return
        print((int(1e10) - ceil(n, 3)))
    elif n % 3 == 1:
        if t != "011" * (n // 3) + "0":
            print((0))
            return
        print((int(1e10) - ceil(n, 3) + 1))
    elif n % 3 == 2:
        if t != "011" * (n // 3) + "01":
            print((0))
            return
        print((int(1e10) - ceil(n, 3)))
else:
    print((0))
