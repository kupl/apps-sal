import numpy as np
import sys
sys.setrecursionlimit(10 ** 9)


def mi():
    return map(int, input().split())


def ii():
    return int(input())


def isp():
    return input().split()


def deb(text):
    print('-------\n{}\n-------'.format(text))


INF = 10 ** 20


class Polynomial:

    def __init__(self, dim=0, const=1):
        self.values = [(dim, const)]

    def __add__(self, other):
        return self.values + other.values


class PolySolver:

    def __init__(self, size):
        self.size = size
        self.f = np.zeros(size, np.int64)
        self.f[0] = 1

    def multiple(self, polynomial, MOD):
        new_F = np.zeros(self.size, np.int64)
        for (dim, const) in polynomial:
            if dim != 0:
                g = np.zeros(self.size, np.int64)
                g[dim:] += self.f[:-dim]
            else:
                g = const * self.f.copy()
            new_F += g
        self.f = new_F
        self.f %= MOD

    def get_coefficient(self, dim):
        return self.f[dim]


def main():
    (N, S) = mi()
    A = list(mi())
    MOD = 998244353
    poly = PolySolver(3010)
    for a in A:
        f = Polynomial(const=2) + Polynomial(dim=a)
        poly.multiple(f, MOD)
    print(poly.get_coefficient(S))


def __starting_point():
    main()


__starting_point()
