import sys
import os


def file_input():
    f = open('Beginner_Contest_162/input.txt', 'r')
    sys.stdin = f


def main():
    (N, K) = list(map(int, input().split()))
    tmp = [0] * (K + 1)
    mod = 10 ** 9 + 7
    out = 0
    for i in range(K, 0, -1):
        tmp[i] = pow(K // i, N, mod)
        for j in range(i * 2, K + 1, i):
            tmp[i] -= tmp[j]
        out += tmp[i] * i
    print(out % mod)


def __starting_point():
    main()


__starting_point()
