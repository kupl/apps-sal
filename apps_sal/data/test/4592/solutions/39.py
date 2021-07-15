import sys
from collections import Counter

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())

    N_MAX = N

    min_factor = list(range(N_MAX + 1))
    min_factor[2::2] = [2] * (N_MAX // 2)
    for i in range(3, int(N_MAX ** 0.5) + 2, 2):
        if min_factor[i] != i:
            continue
        for j in range(i * i, N_MAX + 1, 2 * i):
            if min_factor[j] > i:
                min_factor[j] = i

    def prime_factorize_fast(n):
        a = Counter()
        while n != 1:
            a[min_factor[n]] += 1
            n //= min_factor[n]

        return a

    factors = Counter()

    for n in range(2, N + 1):
        factors += prime_factorize_fast(n)

    ans = 1
    for v in list(factors.values()):
        ans = ans * (v + 1) % MOD

    print(ans)
    return


def __starting_point():
    main()

__starting_point()
