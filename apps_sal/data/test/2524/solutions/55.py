import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    A = list(map(int, input().split()))

    res = 0
    for mask in range(60):
        cnt1 = sum([1 if a & (1 << mask) else 0 for a in A])
        cnt0 = n - cnt1
        res += (pow(2, mask, mod) * cnt1 * cnt0) % mod
        res %= mod
    print(res)


def __starting_point():
    resolve()

__starting_point()
