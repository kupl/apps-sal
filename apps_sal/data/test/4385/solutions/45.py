import numpy as np


def solve(a, b, c, d, e, k):
    arr = np.array([a, b, c, d, e])
    arr, arr2 = [a.flatten() for a in np.meshgrid(arr, arr)]
    arr = np.c_[arr, arr2]
    arr = np.array(list([abs(x[0] - x[1]) for x in arr]))
    print((':(' if arr.max() > k else 'Yay!'))


def __starting_point():
    a, b, c, d, e, k = [int(input()) for _ in range(6)]
    solve(a, b, c, d, e, k)


__starting_point()
