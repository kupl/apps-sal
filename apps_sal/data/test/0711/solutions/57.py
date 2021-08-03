#!/usr/bin/env python3
import sys


MOD = 1000000007  # type: int


def factor(n: int):
    i = 2
    cnt = 0
    while n % i == 0:
        n //= i
        cnt += 1
    if cnt > 0:
        yield i, cnt

    i = 3
    while i * i <= n:
        cnt = 0
        while n % i == 0:
            n //= i
            cnt += 1
        if cnt > 0:
            yield i, cnt
        i += 2

    if n > 1:
        yield n, 1


def comb(n: int, r: int):
    if n - r < r:
        return comb(n, n - r)
    ans = 1
    for i in range(r):
        ans *= n - i
    for i in range(r):
        ans //= i + 1
    return ans


def solve(N: int, M: int):
    ans = 1
    for _p, cnt in factor(M):
        ans *= comb(N - 1 + cnt, cnt) % MOD
        ans %= MOD
    print(ans)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    solve(N, M)


def __starting_point():
    main()


__starting_point()
