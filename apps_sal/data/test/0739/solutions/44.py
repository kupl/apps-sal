import numpy as np
import sys
sys.setrecursionlimit(pow(10, 6))
# input = sys.stdin.readline


def pow_matmul(r, n, m):
    if n == 1:
        return r
    if n % 2 == 0:
        _r = pow_matmul(r, n // 2, m)
        return np.mod(np.dot(_r, _r), m)
    else:
        _r = pow_matmul(r, n // 2, m)
        _r = np.mod(np.dot(_r, _r), m)
        return np.mod(np.dot(r, _r), m)


def main():
    l, a, b, m = list(map(int, input().split()))
    c = [min(max(0, (10**i - a - 1) // b + 1), l) for i in range(19)]
    ans = 0
    r = np.ones((3, 3))
    s = np.array([0, a % m, 1])

    for d in range(1, 19):
        dnum = c[d] - c[d - 1]
        if dnum == 0:
            continue
        r_s = np.array([[pow(10, d, m), 1, 0], [0, 1, (b % m)], [0, 0, 1]])
        r = pow_matmul(r_s, dnum, m)
        s = np.mod(np.dot(r, s), m)
        if c[d] > l:
            break
    print((s[0]))


def __starting_point():
    main()


__starting_point()
