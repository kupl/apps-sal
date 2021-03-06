from itertools import combinations, product
import math
import sys
sysread = sys.stdin.readline
read = sys.stdin.read
sys.setrecursionlimit(10 ** 7)


def run():
    (r1, c1, r2, c2) = map(int, read().split())
    mod = 10 ** 9 + 7

    def generate_inv(n, mod):
        """
        逆元行列
        n >= 2
        Note: mod must bwe a prime number
        """
        ret = [0, 1]
        for i in range(2, n + 1):
            next = -ret[mod % i] * (mod // i)
            next %= mod
            ret.append(next)
        return ret
    inv = generate_inv(10 ** 6 + 1, mod)

    def calc(i, j):
        ret = 0
        agg = 1
        for k in range(1, i + 2):
            agg *= (j + k) % mod
            agg *= inv[k]
            agg %= mod
            ret += agg
        return ret
    ret = 0
    ret += calc(r2, c2)
    ret -= calc(r2, c1 - 1)
    ret -= calc(r1 - 1, c2)
    ret += calc(r1 - 1, c1 - 1)
    ret %= mod
    print(ret)


def __starting_point():
    run()


__starting_point()
