import sys
import numpy as np


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    A = np.array(list(map(int, input().split())), dtype='int64')
    ans = 0
    mod = 10 ** 9 + 7
    for i in range(60):
        q = int((A >> i & 1).sum())
        ans += q * (n - q) * pow(2, i, mod)
        ans %= mod
    print(ans)


def __starting_point():
    main()


__starting_point()
