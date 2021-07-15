# coding: utf-8
import sys
#from operator import itemgetter
sysread = sys.stdin.readline
#from heapq import heappop, heappush
#from collections import defaultdict
sys.setrecursionlimit(10**7)
import math
#from itertools import combinations
def run():
    n,k = map(int, input().split())
    mod = 10 ** 9 + 7
    ret = 0
    inv = generate_inv(n, mod)

    if k >= n-1:
        k = n-1
    left = 1
    right = 1
    ret = 1
    for h in range(1, k+1):
        right *= (n - h) * inv[h]
        right %= mod
        left *= (n - h + 1) * inv[h]
        left %= mod
        ret += right * left
        ret %= mod
    print(ret)


def generate_inv(n,mod):
    """
    逆元行列
    n >= 2
    """
    ret = [0, 1]
    for i in range(2,n+1):
        next = -ret[mod%i] * (mod // i)
        next %= mod
        ret.append(next)
    return ret


def comb_mod(n, a, mod):
    """
    return: [n, a] % mod
    Note: mod must be a prime number
    """
    up = 1
    down = 1
    for i in range(a):
        up *= n - i
        up %= mod
        down *= i + 1
        down %= mod
    down = pow_mod(down, mod - 2, mod)
    return (up * down) % mod

def pow_mod(n, k, mod):
    res = 1
    while True:
        if k // 2 >= 1:
            if k % 2 == 1:
                res = (res * n) % mod
            n = (n ** 2) % mod
            k = k // 2
        else:
            break
    return (n * res) % mod


def __starting_point():
    run()
__starting_point()
