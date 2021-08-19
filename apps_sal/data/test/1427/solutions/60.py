import sys
from math import gcd
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def lcm(a, b):
    return a * b // gcd(a, b)


def resolve():
    n = int(input())
    A = list(map(int, input().split()))
    L = 1
    for a in A:
        L = lcm(L, a)
    res = 0
    for a in A:
        res += L * pow(a, mod - 2, mod)
        res %= mod
    print(res)


def __starting_point():
    resolve()


__starting_point()
