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
    s = read_str()
    dp = np.zeros(2019, dtype=np.int64)
    dp[0] = 1

    cur = 0
    digit = 1

    for i in reversed(s):
        cur = (cur + int(i) * digit) % 2019
        dp[cur] += 1
        digit = digit * 10 % 2019

    print(np.sum([x * (x - 1) // 2 for x in dp]))


if __name__ == '__main__':
    Main()
