import numpy as np
import sys
from decimal import Decimal
import math
from itertools import combinations, product
import bisect
from collections import Counter, deque, defaultdict

# sys.setrecursionlimit(10 ** 6)
MOD = 10 ** 9 + 7
INF = 10 ** 9
PI = 3.14159265358979323846


def read_str(): return sys.stdin.readline().strip()
def read_int(): return int(sys.stdin.readline().strip())
def read_ints(): return map(int, sys.stdin.readline().strip().split())
def read_str_list(): return list(sys.stdin.readline().strip().split())
def read_int_list(): return list(map(int, sys.stdin.readline().strip().split()))
def lcm(a: int, b: int) -> int: return (a * b) // math.gcd(a, b)


def Main():
    n = read_int()
    a = np.array(read_int_list(), np.int64)
    ans = 0
    for i in range(60):
        cnt_one = np.count_nonzero(a >> i & 1)
        cnt_zero = n - cnt_one
        ans += (cnt_one * cnt_zero * (1 << i)) % MOD
        ans %= MOD
    print(ans)


if __name__ == '__main__':
    Main()
