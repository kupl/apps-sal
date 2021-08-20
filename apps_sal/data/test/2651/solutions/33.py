import numpy as np


def main():
    mod = 10 ** 9 + 7
    (n, m) = list(map(int, input().split()))
    X = np.array(list(map(int, input().split())), dtype=np.int64)
    Y = np.array(list(map(int, input().split())), dtype=np.int64)
    dxs = X[1:] - X[:-1]
    left = np.arange(1, n)
    right = np.arange(n - 1, 0, -1)
    x_pattern = left * right % mod
    x_sum = (dxs * x_pattern).sum() % mod
    dys = Y[1:] - Y[:-1]
    up = np.arange(1, m)
    down = np.arange(m - 1, 0, -1)
    y_pattern = up * down % mod
    y_sum = (dys * y_pattern).sum() % mod
    print(x_sum * y_sum % mod)


def __starting_point():
    main()


__starting_point()
