import numpy as np
import sys
input = sys.stdin.readline


def main():
    numbers = []
    n = int(input())
    numbers = np.array(list(map(int, input().split())))

    print((numbers - 1).sum())


def __starting_point():
    main()


__starting_point()
