import sys;      from decimal import Decimal
import math;     from itertools import combinations, product
import bisect;   from collections import Counter, deque, defaultdict

# sys.setrecursionlimit(10 ** 6)
MOD = 10 ** 9 + 7
INF = 10 ** 9
PI = 3.14159265358979323846

def read_str():      return sys.stdin.readline().strip()
def read_int():      return int(sys.stdin.readline().strip())
def read_ints():     return map(int, sys.stdin.readline().strip().split())
def read_str_list(): return list(sys.stdin.readline().strip().split())
def read_int_list(): return list(map(int, sys.stdin.readline().strip().split()))
def lcm(a: int, b: int) -> int: return (a * b) // math.gcd(a, b)

import numpy as np
from numba import njit, i8

@njit(i8(i8))
def dp(N):
    dp = np.full(100005, INF, dtype=np.int64)
    dp[0] = 0
    
    for n in range(1, N + 1):
        pow6 = 1
        while pow6 <= n:
            dp[n] = min(dp[n], dp[n - pow6] + 1)
            pow6 *= 6
        pow9 = 1
        while pow9 <= n:
            dp[n] = min(dp[n], dp[n - pow9] + 1)
            pow9 *= 9
    
    return dp[n]

def Main():
    n = read_int()
    print(dp(n))    

if __name__ ==  '__main__':
    Main()
