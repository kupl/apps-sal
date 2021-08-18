import sys


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


def solve():
    MOD = int(1e9 + 7)
    s = minp()
    n = len(s)
    p = [0] * (n + 1)
    pp = [1] * (n + 1)
    p10 = 1
    for i in range(1, n + 1):
        p[i] = (p[i - 1] + p10 * i) % MOD
        pp[i] = p10
        p10 = (p10 * 10) % MOD
    res = (int(s[0]) * p[n - 1]) % MOD
    for i in range(1, n):
        res = (res + int(s[i]) * (p[n - 1 - i] + pp[n - i] * (i) * (i + 1) // 2)) % MOD
    print(res)


solve()
