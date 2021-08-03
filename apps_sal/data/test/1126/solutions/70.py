import sys
#import time
from collections import deque, Counter, defaultdict
#from fractions import gcd
import bisect
import heapq
#import math
import itertools
import numpy as np
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
inf = 10**18
MOD = 1000000007
def ri(): return int(input())
def rs(): return input().strip()
def rl(): return list(map(int, input().split()))


mod = 998244353

n, x, m = rl()
res = [0] * m
nums = []
cnt = 0
while True:
    if res[x] == 1:
        break
    res[x] = 1
    nums.append(x)

    a = x % m
    x = a * a % m
    cnt += 1
# print(res)
circle = nums.index(x)
if n < circle:
    print(sum(nums[:circle]))
else:
    times = (n - circle) // (cnt - circle)
    last = (n - circle) % (cnt - circle)
    # print(times)
    # print(last)
    # print(circle)
    print(sum(nums[:circle]) + sum(nums[circle:]) * times + sum(nums[circle:circle + last]))
