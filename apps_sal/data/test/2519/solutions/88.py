import sys
from collections import deque, Counter, defaultdict
import bisect
import heapq
import math
import itertools
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
inf = 10 ** 18
MOD = 1000000007


def ri():
    return int(input())


def rs():
    return input().strip()


def rl():
    return list(map(int, input().split()))


mod = 998244353
'\n1 3 3 10 15\n1 1.5 1.5 2.5 3 \n'
(n, k) = rl()
p = rl()
sum_ = 0
(cum, ans, ser) = ([], [], [])
for i in range(1, 2000):
    sum_ += i
    cum.append(sum_ / i)
for i in p:
    ans.append(cum[i - 1])
cs = [0]
for i in range(n):
    cs.append(cs[i] + ans[i])
for i in range(n + 1 - k):
    ser.append(cs[i + k] - cs[i])
print(max(ser))
