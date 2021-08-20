import numpy as np


def main():
    MOD = 10 ** 9 + 7
    limit = 60
    N = int(input())
    A = np.array(input().split(), dtype=np.int64)
    ans = 0
    for n in range(limit):
        res = A & 1 << n
        x = np.count_nonzero(res)
        y = N - x
        x *= y
        for _ in range(n):
            x *= 2
            x %= MOD
        ans += x
    print(ans % MOD)


def __starting_point():
    main()


__starting_point()
