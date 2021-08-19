# -*-coding:utf-8-*-
import numpy as np
import sys
input = sys.stdin.readline


def main():
    numbers = []
    n, m = map(int, input().split())
    [numbers.append(int(input())) for _ in range(n)]
    n_numbers = np.array(numbers, dtype=int)
    n_numbers.sort()
    print(min(n_numbers[i + m - 1] - n_numbers[i] for i in range(n - m + 1)))


def __starting_point():
    main()


__starting_point()
