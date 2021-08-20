import sys
from math import gcd
from copy import deepcopy
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def lcm(a, b):
    return a * b // gcd(a, b)


def resolve():
    (n, m) = list(map(int, input().split()))
    A = list(map(int, input().split()))
    A_ = deepcopy(A)
    cnt = [0] * n
    for i in range(n):
        while A_[i] % 2 == 0:
            A_[i] //= 2
            cnt[i] += 1
        if i != 0 and cnt[i] != cnt[i - 1]:
            print(0)
            return
    L = 1
    for a in A:
        L = lcm(L, a // 2)
    res = m // L - m // (L * 2)
    print(res)


def __starting_point():
    resolve()


__starting_point()
