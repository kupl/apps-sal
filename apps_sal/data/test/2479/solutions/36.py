import numpy as np
# from numba import njit
# from numba.types import int64
i8 = np.int64


# @njit((int64, int64[:,::-1]), cache=True)
def solve(n, qr):
    col = np.zeros(n - 1, i8)
    col[0] = 0
    col_min = n - 1
    row = np.zeros(n - 1, i8)
    row[0] = 0
    row_min = n - 1
    white = 0
    for i in range(qr.shape[0]):
        j = qr[i, 1] - 1
        if qr[i, 0] == 1:
            if j < col_min:
                white += row_min - 1
                for m in range(j + 1, col_min):
                    col[m] = row_min - 1
                col_min = j
            else:
                white += col[j]
        else:
            if j < row_min:
                white += col_min - 1
                for m in range(j + 1, row_min):
                    row[m] = col_min - 1
                row_min = j
            else:
                white += row[j]
    return white


def main():
    f = open(0)
    n, q = [int(x) for x in f.readline().split()]
    qr = np.fromstring(f.read(), i8, sep=' ').reshape((-1, 2))
    white = solve(n, qr)
    print((n - 2) ** 2 - white)

main()
