import numpy as np
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines


def main():
    (n, m, k) = map(int, input().split())
    a = np.array(readline().split(), np.int64)
    b = np.array(readline().split(), np.int64)
    aa = np.zeros(n + 1, np.int64)
    ba = np.zeros(m + 1, np.int64)
    aa[1:] = a.cumsum()
    ba[1:] = b.cumsum()
    aa = aa[aa <= k]
    ba = ba[ba <= k]
    rs = np.searchsorted(ba, k - aa, side='right') - 1
    rs += np.arange(len(aa))
    r = rs.max()
    print(r)


def __starting_point():
    main()


__starting_point()
