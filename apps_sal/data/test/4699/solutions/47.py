import sys
import numpy as np
read = sys.stdin.readline


def main(n, k, a):
    for i in np.arange(n, 100000):
        ok = True
        for j in str(i):
            ok &= j not in a
        if ok:
            print(i)
            break


def __starting_point():
    n, k = np.fromstring(read(), dtype=np.int32, sep=' ')
    a = set(read().split())
    main(n, k, a)


__starting_point()
