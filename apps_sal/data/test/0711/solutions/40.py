import sys
import math
from collections import defaultdict
from collections import deque
sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def NI():
    return int(input())


def NMI():
    return map(int, input().split())


def NLI():
    return list(NMI())


def SI():
    return input()


def prime_fact(n):
    root = int(math.sqrt(n))
    prime_dict = {}
    for i in range(2, root + 1):
        cnt = 0
        while n % i == 0:
            cnt += 1
            n = n // i
        if cnt:
            prime_dict[i] = cnt
    if n != 1:
        prime_dict[n] = 1
    return prime_dict


def combination_mod_initialize(n, MOD=10 ** 9 + 7):
    fac = [1] * (n + 1)
    inv = [1] * (n + 1)
    for i in range(1, n + 1):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = inv[i - 1] * pow(i, -1, MOD) % MOD
    return (fac, inv)


def combination_mod(n, r, fac, inv, mod=10 ** 9 + 7):
    return fac[n] * inv[r] * inv[n - r]


def main():
    (N, M) = NMI()
    PD = prime_fact(M)
    ans = 1
    (fac, inv) = combination_mod_initialize(10 ** 6, MOD)
    for x in list(PD.values()):
        ans = ans * combination_mod(N + x - 1, N - 1, fac, inv) % MOD
    print(ans)


def __starting_point():
    main()


__starting_point()
