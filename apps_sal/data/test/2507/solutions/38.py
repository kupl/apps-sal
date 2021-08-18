
import numpy as np


def resolve():
    def check(X):
        a = X // F
        diff = np.maximum(A - a, 0)
        cnt = np.sum(diff)
        return cnt <= K

    N, K = list(map(int, input().split()))
    A = np.array(input().split(), np.int64)
    F = np.array(input().split(), np.int64)

    A.sort()
    F.sort()
    F = F[::-1]

    ok = 10 ** 12
    ng = -1
    while ok - ng > 1:
        X = (ok + ng) // 2
        if check(X):
            ok = X
        else:
            ng = X

    print(ok)


def __starting_point():
    resolve()


__starting_point()
