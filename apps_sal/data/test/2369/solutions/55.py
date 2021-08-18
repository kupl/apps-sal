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


def combinations_mod(n, r, mod=1000000007):
    """Returns nCr in mod."""
    r = min(r, n - r)
    combs = 1
    for i, j in zip(range(n - r + 1, n + 1), range(1, r + 1)):
        combs *= (i % mod) * pow(j, mod - 2, mod)
        combs %= mod
    return combs


def main():
    N, K = NMI()
    A = NLI()
    A.sort()
    ans = 0
    fac = [1] * (N + 1)
    inv = [1] * (N + 1)

    for i in range(1, N + 1):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = inv[i - 1] * pow(i, -1, MOD) % MOD

    for i in range(N):
        max_num = 0
        min_num = 0
        if i >= K - 1:
            max_num = fac[i] * inv[K - 1] * inv[i - K + 1]
        if N - 1 - i >= K - 1:
            min_num = fac[N - 1 - i] * inv[K - 1] * inv[N - K - i]
        ans += (max_num - min_num) * A[i] % MOD
    print(ans % MOD)


def __starting_point():
    main()


__starting_point()
