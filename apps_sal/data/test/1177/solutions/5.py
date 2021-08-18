from sys import stdin
mod = 998244353


def solveAsPolynomial():
    import numpy as np
    N, S = list(map(int, stdin.readline().split()))
    a = list(map(int, stdin.readline().split()))
    ans = 0
    f = np.zeros(S + 1, np.int64)
    for A in a:
        f[0] += 1
        f[A:] += f[:-A].copy()
        f %= mod
        ans += f[S]
        ans %= mod
    return ans


def main():
    ans = solveAsPolynomial()
    print(ans)


def __starting_point():
    main()


__starting_point()
