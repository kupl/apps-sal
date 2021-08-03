import sys
import math
import fractions
def input(): return sys.stdin.readline().rstrip()


mod = 10**9 + 7


def factorize(n):
    b = 2
    fct = dict()
    while b * b <= n:
        while n % b == 0:
            n //= b
            if b in fct:
                fct[b] += 1
            else:
                fct[b] = 1
        b = b + 1
    if n > 1:
        if b in fct:
            fct[n] += 1
        else:
            fct[n] = 1
    return fct


def divmod(x, mod=10**9 + 7):
    return pow(x, mod - 2, mod)


def solve():

    N = int(input())
    A = list(map(int, input().split()))
    B = [[1] for _ in range(N)]

    fac_list = dict()
    for i in range(N):
        d = factorize(A[i])
        for k, v in list(d.items()):
            fac_list[k] = max(fac_list.get(k, 0), v)

    lcm = 1
    for k, v in list(fac_list.items()):
        lcm *= (k**v)
        lcm %= mod

    ans = 0
    for i in range(N):
        ans += divmod(A[i])
        ans %= mod

    ans *= lcm
    ans %= mod
    print(ans)


def __starting_point():
    solve()


__starting_point()
