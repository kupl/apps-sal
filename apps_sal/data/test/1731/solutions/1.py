import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline
MOD = 10 ** 9 + 7
MAX_N = 2000


def single_mod_nCr(n, r):
    if n < r or n < 0 or r < 0:
        return 0
    if r > n - r:
        r = n - r
    ret = 1
    for i in range(r):
        ret *= n - i
        ret *= pow(i + 1, MOD - 2, MOD)
        ret %= MOD
    return ret


(n, m) = [int(item) for item in input().split()]
print(single_mod_nCr(n + m * 2 - 1, m * 2))
