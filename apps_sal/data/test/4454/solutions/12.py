from math import ceil, floor, log, sqrt, factorial, pow, pi, gcd, log10, atan, tan
import sys
inf = float('inf')
(mod, MOD) = (1000000007, 998244353)


def get_array():
    return list(map(int, sys.stdin.readline().strip().split()))


def get_ints():
    return map(int, sys.stdin.readline().strip().split())


def input():
    return sys.stdin.readline().strip()


T = int(input())
while T:
    n = int(input())
    Arr = get_array()
    s = sum(Arr)
    ans = ceil(s / n)
    print(ans)
    T -= 1
