#!/usr/bin/env python3
def main():
    N, K = list(map(int, input().split()))
    mod = 7 + 10 ** 9

    res = 0
    for k in range(K, N + 2):
        res += ((k * (2 * N - k + 1) / 2) - (k * (k - 1) / 2) + 1)
        res %= mod
    print((int(res)))


def __starting_point():
    main()


__starting_point()
