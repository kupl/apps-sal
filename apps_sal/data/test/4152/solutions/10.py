import sys
from collections import Counter


def main():
    n = int(input())
    ar = list(map(int, input().split()))

    res = n
    freq = Counter(ar)

    for val in ar:
        for d in range(32):
            x = (1 << d) - val
            if x <= 0 or not freq.get(x):
                continue

            count = freq.get(x) - (x == val)
            if count > 0:
                res -= 1
                break

    print(res)


def __starting_point():
    main()


__starting_point()
