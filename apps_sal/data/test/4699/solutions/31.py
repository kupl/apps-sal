import sys
import numpy as np
read = sys.stdin.readline


def main(n, k, a):
    for i in range(n, 100000):
        s = np.array(list(map(int, str(i))), dtype=np.int64)
        ok = True
        for j in s:
            ok &= j not in a
        if ok:
            print(i)
            break


def __starting_point():
    (n, k) = np.fromstring(read(), dtype=np.int64, sep=' ')
    a = np.fromstring(read(), dtype=np.int64, sep=' ')
    main(n, k, a)


__starting_point()
