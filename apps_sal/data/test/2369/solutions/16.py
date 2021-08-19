import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
def input(): return sys.stdin.readline().strip()
def NI(): return int(input())
def NMI(): return map(int, input().split())
def NLI(): return list(NMI())
def SI(): return input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]

# 二項係数計算用　階乗と逆元の初期化


def combination_mod_initialize(n, MOD=10**9 + 7):
    fac = [1] * (n + 1)
    inv = [1] * (n + 1)
    for i in range(1, n + 1):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = inv[i - 1] * pow(i, -1, MOD) % MOD
    return fac, inv

# 二項係数　高速


def combination_mod(n, r, fac, inv):
    return fac[n] * inv[r] * inv[n - r]


def main():
    N, K = NMI()
    A = NLI()
    A.sort()
    ans = 0
    fac, inv = combination_mod_initialize(N, MOD)

    for i in range(N):
        max_num = 0
        min_num = 0
        if i >= K - 1:
            max_num = combination_mod(i, K - 1, fac, inv)
        if N - 1 - i >= K - 1:
            min_num = combination_mod(N - 1 - i, K - 1, fac, inv)
        ans += (max_num - min_num) * A[i] % MOD
    print(ans % MOD)


def __starting_point():
    main()


__starting_point()
