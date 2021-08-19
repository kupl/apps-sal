import sys
import itertools
import queue
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def read_values():
    return list(map(int, input().split()))


def read_index():
    return [int(x) - 1 for x in input().split()]


def read_list():
    return list(read_values())


def read_lists(N):
    return [read_list() for n in range(N)]


class V:

    def __init__(self, f, v=None):
        self.f = f
        self.v = v

    def __str__(self):
        return str(self.v)

    def ud(self, n):
        if self.v is None:
            self.v = n
        else:
            self.v = self.f(self.v, n)


def mat_mul(X, Y, mod):
    m = len(X)
    return [[sum((X[i][k] * Y[k][j] % mod for k in range(m))) % mod for j in range(m)] for i in range(m)]


def mat_pow(M, k, mod):
    m = len(M)
    res = [[1 if i == j else 0 for j in range(m)] for i in range(m)]
    while k > 0:
        if k & 1:
            res = mat_mul(M, res, mod)
        M = mat_mul(M, M, mod)
        k >>= 1
    return res


def main():
    (L, A, B, M) = read_values()
    res = 0
    D = [(0, 0)]
    for d in range(1, 20):
        l = D[-1][1]
        r = max(0, min((10 ** d - 1 - A) // B + 1, L))
        D.append((l, r))
    res = 0
    c = 0
    R = [0, A, 1]
    Mat = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    for d in range(1, 20):
        num = D[d][1] - D[d][0]
        MM = [[10 ** d, 0, 0], [1, 1, 0], [0, B, 1]]
        Mat = mat_mul(Mat, mat_pow(MM, num, M), M)
    X = sum((R[i] * Mat[i][0] % M for i in range(3))) % M
    print(X)


def __starting_point():
    main()


__starting_point()
