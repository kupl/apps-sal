import numpy as np
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines


def main():
    n = int(input())
    if n == 1:
        print(1)
        return
    divs = np.arange(1, n + 1)
    divs2 = n // divs
    divs3 = divs2 * (divs2 + 1) // 2
    divs3 = divs3 * divs
    r = divs3.sum()
    print(r)


def __starting_point():
    main()


__starting_point()
