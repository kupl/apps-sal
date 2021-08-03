from collections import Counter, defaultdict
import numpy as np
import sys
read = sys.stdin.read
readlines = sys.stdin.readlines


def main():
    n, *a = map(int, read().split())
    aa = Counter(a)
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    for k, v in aa.items():
        d1[k] = v * (v - 1) // 2
        v -= 1
        d2[k] = v * (v - 1) // 2
    sumd1 = sum(d1.values())
    for ae in a:
        r = sumd1 - d1[ae] + d2[ae]
        print(r)


def __starting_point():
    main()


__starting_point()
