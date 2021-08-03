import sys
import math
# import bisect
# import numpy as np
# from decimal import Decimal
# from numba import njit, i8, u1, b1 #JIT compiler
# from itertools import combinations, product
# from collections import Counter, deque, defaultdict

# sys.setrecursionlimit(10 ** 6)
MOD = 10 ** 9 + 7
INF = 10 ** 9
PI = 3.14159265358979323846


def read_str(): return sys.stdin.readline().strip()
def read_int(): return int(sys.stdin.readline().strip())
def read_ints(): return map(int, sys.stdin.readline().strip().split())
def read_ints2(x): return map(lambda num: int(num) - x, sys.stdin.readline().strip().split())
def read_str_list(): return list(sys.stdin.readline().strip().split())
def read_int_list(): return list(map(int, sys.stdin.readline().strip().split()))
def GCD(a: int, b: int) -> int: return b if a % b == 0 else GCD(b, a % b)
def LCM(a: int, b: int) -> int: return (a * b) // GCD(a, b)


def factorization(num):
    prime = []
    n = num
    p = 2
    while p * p <= num:
        if n % p == 0:
            cnt = 0
            while n % p == 0:
                cnt += 1
                n //= p
            prime.append((p, cnt))
        p += 1
    if n != 1:
        prime.append((n, 1))
    if not prime:
        prime.append((num, 1))
    return prime


def Main():
    a, b = read_ints()
    g = math.gcd(a, b)
    if g == 1:
        print(1)
        return
    prime = factorization(g)
    print(len(prime) + 1)


def __starting_point():
    Main()


__starting_point()
