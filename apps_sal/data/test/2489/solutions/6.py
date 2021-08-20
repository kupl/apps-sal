from collections import Counter
import numpy as np
import sys
read = sys.stdin.read
readlines = sys.stdin.readlines


def main():
    (n, *a) = list(map(int, read().split()))
    if 1 in a:
        count1 = a.count(1)
        if count1 == 1:
            print(1)
            return
        else:
            print(0)
            return
    a = np.array(a)
    maxa = a.max()
    seq = np.zeros(maxa + 1, np.int32)
    (u, cnt) = np.unique(a, return_counts=True)
    for (ue, cnte) in zip(u, cnt):
        if cnte == 1:
            seq[ue] = 1
    for ae in a:
        t = ae * 2
        while t <= maxa:
            seq[t] = 0
            t += ae
    r = seq.sum()
    print(r)


def __starting_point():
    main()


__starting_point()
