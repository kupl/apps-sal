import sys
import numpy as np
read = sys.stdin.readline


def main(n, k, a):
    for i in np.arange(n, 100000):
        ok = True
        j = i
        while j:
            ok &= j % 10 not in a
            j //= 10
        if ok:
            print(i)
            break


def __starting_point():
    n, k = np.fromstring(read(), dtype=np.int32, sep=' ')
    a = np.fromstring(read(), dtype=np.int32, sep=' ')
    main(n, k, a)


__starting_point()
