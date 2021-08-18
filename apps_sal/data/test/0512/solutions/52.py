import numpy as np
from numpy import int8, int32, int64


def solve_core(N, ca, cb, dp):
    def check(n, d):
        k = 2 * n
        for m in range(k, k + d):
            if cb[m] > 0:
                return 0
            if ca[m] > 0 and ca[m] != d:
                return 0
            if ca[m] == -1 and cb[m + d] > 0:
                return 0
        for m in range(k + d, k + 2 * d):
            if ca[m] != 0:
                return 0
        return 1

    for i in range(N - 1, -1, -1):
        dp[i] = 0
        for j in range(i + 1, N + 1):
            d = j - i
            if dp[j] and check(i, d):
                dp[i] = 1
                break
    return dp[0]


def solve(N, ab):
    ca = np.zeros(2 * N, dtype=int64)
    cb = np.zeros(2 * N, dtype=int64)

    for i in range(ab.shape[0]):
        a = ab[i, 0]
        b = ab[i, 1]
        if a > - 1 and b > -1:
            if b - a <= 0:
                return 0
            if ca[a] != 0 or cb[a] > 0 or ca[b] != 0 or cb[b] > 0:
                return 0
            ca[a] = b - a
            cb[b] = 1
        elif a > -1:
            if ca[a] != 0 or cb[a] > 0:
                return 0
            ca[a] = -1
        elif b > -1:
            if ca[b] != 0 or cb[b] > 0:
                return 0
            cb[b] = 1

    dp = np.empty(N + 1, dtype=int64)
    dp[N] = 1
    return solve_core(N, ca, cb, dp)


def main(in_file):
    f = open(in_file)
    N = int(f.readline())
    ab = np.fromstring(f.read(), dtype=int64, sep=' ')
    ab -= 1
    ab = ab.reshape((-1, 2))
    ans = solve(N, ab)
    return ans


def __starting_point():
    ans = main(0)
    print('Yes' if ans else 'No')


__starting_point()
