import numpy as np


def main():
    (n, k) = map(int, input().split())
    p = [list(map(str, input().split())) for _ in range(n)]
    arr = [[[0] * 2 for j in range(k)] for i in range(k)]
    for i in range(n):
        (x, y, c) = p[i]
        (x, y) = (int(x), int(y))
        (mx, my) = (x % k, y % k)
        f = False
        if x // k % 2 != y // k % 2:
            f = not f
        if c == 'W':
            f = not f
        if f:
            arr[0][0][0] += 1
            arr[mx][0][0] -= 1
            arr[0][my][0] -= 1
            arr[mx][my][0] += 2
        else:
            arr[0][my][0] += 1
            arr[mx][0][0] += 1
            arr[mx][my][0] -= 2
        f = False
        if x // k % 2 != y // k % 2:
            f = not f
        if c == 'B':
            f = not f
        if f:
            arr[0][0][1] += 1
            arr[mx][0][1] -= 1
            arr[0][my][1] -= 1
            arr[mx][my][1] += 2
        else:
            arr[0][my][1] += 1
            arr[mx][0][1] += 1
            arr[mx][my][1] -= 2
    np_arr = np.array(arr)
    np_arr = np.cumsum(np_arr, axis=0)
    np_arr = np.cumsum(np_arr, axis=1)
    print(int(np.max(np_arr)))


def __starting_point():
    main()


__starting_point()
