#  --*-coding:utf-8-*--

import math


def main():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))

    s = sum(A)

    D1 = []
    D2 = []

    for i in range(1, int(math.sqrt(s)) + 1):
        if s % i == 0:
            D1.append(s // i)
            D2.append(i)

    for d in D1 + list(reversed(D2)):
        B = sorted([a % d for a in A])
        x = sum(B[:-sum(B) // d])

        if x <= K:
            print(d)
            return


main()
