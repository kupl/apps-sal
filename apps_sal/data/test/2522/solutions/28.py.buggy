from collections import Counter
import numpy as np


def main():
    n = int(input())
    a = np.array([int(i) for i in input().split()])
    b = np.array([int(i) for i in input().split()])
    ca = Counter(a)
    cb = Counter(b)
    for k in list(cb.keys()):
        if cb[k] > n - ca[k]:
            print("No")
            return
    while any(a == b):
        s = max(ca[k] for k in list(cb.keys()))
        b = np.roll(b, s)
    print("Yes")
    print((*b))


def __starting_point():
    main()


__starting_point()
