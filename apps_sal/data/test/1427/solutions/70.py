from math import gcd
from functools import reduce


def resolve():

    def lcm_base(x, y):
        return x * y // gcd(x, y)

    def lcm_list(arr):
        return reduce(lcm_base, arr, 1)
    MOD = 10 ** 9 + 7
    N = int(input())
    A = list(map(int, input().split()))
    num = lcm_list(A) % MOD
    ans = 0
    for a in A:
        ans += num * pow(a, MOD - 2, MOD) % MOD
    ans %= MOD
    print(ans)


def __starting_point():
    resolve()


__starting_point()
