import sys

input = sys.stdin.readline


def read_values():
    return list(map(int, input().split()))


def read_list():
    return list(read_values())


def func(N, mod):
    F = [1]
    for i in range(1, N + 1):
        F.append(F[-1] * i % mod)
    return F


INV = {}


def inv(a, mod):
    if a in INV:
        return INV[a]
    r = pow(a, mod - 2, mod)
    INV[a] = r
    return r


def C(F, a, b, mod):
    return F[a] * inv(F[b], mod) * inv(F[a - b], mod) % mod


def main():
    mod = 10 ** 9 + 7
    N, M = read_values()
    X = read_list()
    Y = read_list()

    res_x = 0
    for i in range(N - 1):
        res_x += (i + 1) * (N - i - 1) * (X[i + 1] - X[i]) % mod
        res_x %= mod

    res_y = 0
    for i in range(M - 1):
        res_y += (i + 1) * (M - i - 1) * (Y[i + 1] - Y[i]) % mod
        res_y %= mod
    print((res_x * res_y % mod))


def __starting_point():
    main()


__starting_point()
