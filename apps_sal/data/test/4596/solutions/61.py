# -*-coding:utf-8-*-
import numpy as np
import sys
input = sys.stdin.readline


def main():
    n = input()
    A = np.array(input().split(), dtype=np.int32)
    answer = 0

    while np.all(A % 2 == 0):
        A //= 2
        answer += 1
    print(answer)


def __starting_point():
    main()


__starting_point()
