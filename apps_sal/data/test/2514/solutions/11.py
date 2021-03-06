from collections import Counter
import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    S = sum(A)
    cunt_A = Counter(A)
    for q in range(Q):
        (b, c) = map(int, input().split())
        S += (c - b) * cunt_A[b]
        cunt_A[c] += cunt_A[b]
        cunt_A[b] = 0
        print(S)


def __starting_point():
    main()


__starting_point()
