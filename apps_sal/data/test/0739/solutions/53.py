import sys
import time

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    import numpy as np
    l, a, b, m = list(map(int, readline().split()))
    d_min = len(str(a))
    d_max = len(str(a + (l - 1) * b))
    count_d = [-1] * 19

    prev = -1
    for i in range(d_min, d_max + 1):
        power = 10 ** i
        ok = 0
        ng = l + 1
        while abs(ng - ok) > 1:
            mid = (ok + ng) // 2
            x = a + mid * b
            if x < power:
                ok = mid
            else:
                ng = mid
        ok = min(ok, l - 1)
        count_d[i] = ok - prev
        prev = ok

    res = np.array([0, a, 1], dtype="int64")
    res = np.mod(res, m)

    for i in range(19):
        count = count_d[i]
        if count == -1:
            continue
        mat = np.array([[10 ** i, 0, 0],
                        [1, 1, 0],
                        [0, b, 1]], dtype="int64")
        mat = np.mod(mat, m)
        cur = np.eye(3, dtype="int64")
        count_bit = format(count, "b")
        for bit in count_bit[::-1]:
            if bit == "1":
                cur = np.dot(cur, mat)
                cur = np.mod(cur, m)
            mat = np.dot(mat, mat)
            mat = np.mod(mat, m)
        res = np.dot(res, cur)
        res = np.mod(res, m)

    print((res[0]))


def __starting_point():
    main()

__starting_point()
