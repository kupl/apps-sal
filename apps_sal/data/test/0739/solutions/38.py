import numpy as np
import math

L, A, B, M = list(map(int, input().split()))


def f(i):
    return A + B * i


def Cd(d):
    return bisect(-1, L, d + 1) - bisect(-1, L, d)


def is_ok(i, d):
    return len(str(f(i))) >= d


def bisect(ng, ok, d):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid, d):
            ok = mid
        else:
            ng = mid
    return ok


def pow_mat(a, x, p=math.inf):
    ret = np.eye(a.shape[0], dtype=int)
    tmp = a
    for i in range(x.bit_length()):
        if x >> i & 1:
            ret = np.mod(ret @ tmp, p)
        tmp = np.mod(tmp @ tmp, p)
    return ret


ret = np.eye(3, dtype=int)
for d in range(1, 19):
    a = np.array([[pow(10, d, M), 0, 0],
                  [1, 1, 0],
                  [0, B, 1]], dtype=int)
    ret = np.mod(ret @ pow_mat(a, Cd(d), M), M)
print((np.mod(np.array([0, A % M, 1]) @ ret, M)[0]))
